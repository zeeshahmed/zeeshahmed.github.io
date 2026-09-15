#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Generate the hero S21 trace for index.qmd.

The curve is a sum of Lorentzian dips, one per resonator, with jittered centres,
depths and widths so it reads as a measurement rather than as an illustration.
Writes _hero.qmd, which index.qmd includes inline; inlining rather than linking
an <img> matters because an SVG animation inside an <img> restarts on repaint.

    ./tools/make-hero.py        # rewrites _hero.qmd in the repo root
"""
import math
import pathlib
import random

random.seed(20260914)

W, H = 900.0, 110.0
N_RES = 42
PAD_L, PAD_R = 8.0, 8.0
Y_BASE, Y_FLOOR = 15.0, 99.0     # y of 0 dB, and y of DB_FLOOR
DB_FLOOR = 19.0

span = W - PAD_L - PAD_R
resonators = []
for i in range(N_RES):
    centre = PAD_L + span * (i + 0.5) / N_RES + random.uniform(-0.38, 0.38) * span / N_RES
    depth = random.uniform(5.0, 17.0)
    hwhm = random.uniform(0.7, 1.8)
    resonators.append((centre, depth, hwhm))


def attenuation(x: float) -> float:
    """Total attenuation in dB at horizontal position x."""
    total = sum(d / (1.0 + ((x - c) / g) ** 2) for c, d, g in resonators)
    total += 0.55 * math.sin(x / 61.0) + 0.3 * math.sin(x / 17.0 + 1.1)
    return total + random.gauss(0, 0.1)


scale = (Y_FLOOR - Y_BASE) / DB_FLOOR
STEPS = 2600
samples = []
for k in range(STEPS + 1):
    x = PAD_L + span * k / STEPS
    y = min(max(Y_BASE + attenuation(x) * scale, 2.0), H - 2.0)
    samples.append((x, y))

kept = [samples[0]]
for p in samples[1:-1]:
    if abs(p[1] - kept[-1][1]) > 0.22 or p[0] - kept[-1][0] > 4.0:
        kept.append(p)
kept.append(samples[-1])

d = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in kept)
length = sum(math.dist(kept[i - 1], kept[i]) for i in range(1, len(kept)))
dash = math.ceil(length) + 20

fragment = f'''```{{=html}}
<div class="s21">
<svg id="hero-s21" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}"
     role="img" aria-label="A microwave transmission measurement: a flat baseline interrupted by about forty narrow resonance dips, one per readout channel.">
  <style>
    #hero-s21 .trace {{
      fill: none;
      stroke: #0e7c86;
      stroke-width: 1.15;
      stroke-linejoin: round;
      stroke-linecap: round;
      stroke-dasharray: {dash};
      stroke-dashoffset: {dash};
      animation: s21sweep 2.6s cubic-bezier(.22,.61,.36,1) .25s forwards;
    }}
    #hero-s21 .axis {{ fill: none; stroke: #dde3e9; stroke-width: 1; }}
    @keyframes s21sweep {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      #hero-s21 .trace {{ animation: none; stroke-dashoffset: 0; }}
    }}
  </style>
  <path class="axis" d="M8 {H - 1.5:.1f} H {W - 8:.0f}"/>
  <path class="trace" d="{d}"/>
</svg>
</div>
```
'''

out = pathlib.Path(__file__).resolve().parent.parent / "_hero.qmd"
out.write_text(fragment)
print(f"{len(kept)} points, path length {length:.0f} -> {out}")
