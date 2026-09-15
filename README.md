# zeeshahmed.github.io

Personal research site for Zeeshan Ahmed, SLAC National Accelerator Laboratory and Stanford
University. Built with [Quarto](https://quarto.org) and deployed to GitHub Pages by GitHub
Actions.

## Build

Quarto is installed at `~/.local/opt/quarto/bin/quarto` on the authoring machine.

```bash
~/.local/opt/quarto/bin/quarto preview   # live reload on localhost
~/.local/opt/quarto/bin/quarto render    # writes _site/
```

Pushing to `main` runs `.github/workflows/publish.yml`, which renders the site and deploys
`_site` via the native Pages deployment. The repository's Pages source must be set to
**GitHub Actions** in Settings → Pages.

## Layout

```
_quarto.yml                 site config, navbar, fonts
index.qmd                   hook, hero trace, three research threads, recent items
about.qmd                   bio, current roles, education, contact
research.qmd                the three scientific questions
smurf.qmd                   the readout platform
devices.qmd                 fabrication program and the DMF
group.qmd                   members, alumni, recruiting
publications.qmd            selected list plus links out
outreach.qmd                talks, public lectures, outreach
styles.scss                 the single stylesheet: palette, type, layout
images/                     photographs and the generated hero SVG
CLAUDE.md                   quarterly maintenance procedure
```

`CLAUDE.md` is the file to read before editing content. It records which facts are settled,
which change, and what must not be asserted.

## Outstanding

- `cv.pdf` is linked from `index.qmd` and `about.qmd` but is not yet in the repository.
- Photo credits are confirmed only for the two KIPAC images. Others carry descriptive
  captions and no attribution.
- Items still marked with `.todo` callouts: SMuRF hardware photograph, DMF facility URL and
  an operations photograph, alumni placements, press coverage 2024–2026.
