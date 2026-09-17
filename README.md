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
inflation.qmd               the inflation search, South Pole Observatory
structure.qmd               CMB lensing and large-scale structure, Simons Observatory
smurf.qmd                   the readout platform
devices.qmd                 fabrication program and the DMF
group.qmd                   members, alumni, recruiting
publications.qmd            selected list plus links out
outreach.qmd                talks, public lectures, outreach
styles.scss                 the single stylesheet: palette, type, layout
_hero.qmd                   generated inline hero SVG, included by index.qmd
tools/make-hero.py          regenerates _hero.qmd
images/                     photographs
```

Maintenance notes live in `CLAUDE.md` in the parent directory, outside this repository.
Read it before editing content: it records which facts are settled and which need checking
each quarter.

## Outstanding

- One `.todo` callout remains, visible only under the draft profile
  (`quarto preview --profile draft`): two unconfirmed alumni placements on group.qmd.
- Photo credits are on five images; the rest carry none yet.
