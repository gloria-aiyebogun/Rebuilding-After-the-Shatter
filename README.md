# Rebuilding after the Shatter

**A Woman's Guide to Healing from Heartbreak, Reclaiming Her Worth, and Living in Emotional Freedom**

*by Gloria Ichoja Aiyebogun*

---

## About the Book

Heartbreak doesn't just break your heart. It shakes your identity, silences your voice, and leaves you wondering if you will ever feel whole again.

*Rebuilding after the Shatter* is a compassionate, practical guide for every woman who has loved deeply and been left broken. Written by a psychologist with nearly a decade of counselling experience, this book walks with you through the full journey of healing — from understanding your pain, to releasing the past, to reclaiming your worth and opening your heart again.

With eight gentle chapters and a personal reflection exercise in each one, this is not a book you simply read. It is a companion you return to — on the hard days, the quiet days, and the days when you finally begin to feel like yourself again.

**You are not broken. You are becoming.**

---

## Read Online

The full book is freely available to read at:

**https://gloria-aiyebogun.github.io/Rebuilding-After-the-Shatter/**

---

## Get the Book

| Format | Link |
|---|---|
| Kindle ebook (Amazon) | *(coming soon)* |
| Paperback (Amazon) | *(coming soon)* |
| EPUB (free download) | [Latest Release](https://github.com/gloria-aiyebogun/Rebuilding-After-the-Shatter/releases/latest) |
| PDF (free download) | [Latest Release](https://github.com/gloria-aiyebogun/Rebuilding-After-the-Shatter/releases/latest) |

---

## About the Author

**Gloria Ichoja Aiyebogun** holds a Bachelor of Science in General and Applied Psychology and a Master's degree in Social and Terrorism Psychology, both from the University of Jos, Nigeria. She is a public health and mental health practitioner with expertise in psychological wellbeing, trauma, and community-based advocacy.

For nearly a decade she worked as an online counsellor for adolescents, and has conducted research on gender-based violence with NGOs across Nigeria. She lives in Abuja, Nigeria.

---

## Contents

1. Understanding the Pain
2. Breaking the Silence
3. Letting Go Without Losing Yourself
4. Healing the Wounds You Can't See
5. Rebuilding Self-Worth
6. Becoming Whole Again
7. Opening Your Heart Again
8. Living in Emotional Freedom

---

## Repository Structure

This book is written in [Quarto](https://quarto.org/) and outputs to:

- **HTML** — hosted on GitHub Pages (web reading)
- **EPUB** — for Kindle and ebook readers
- **PDF** — for print (6 × 9 in paperback, KDP-ready)

```
.
├── _quarto.yml          # Project configuration
├── index.qmd            # Title & dedication
├── copyright.qmd        # Copyright page
├── intro.qmd            # Introduction
├── chapter1.qmd – chapter8.qmd
├── about.qmd            # About the author
├── acknowledgements.qmd
├── references.qmd       # Further reading
├── epub.css             # EPUB styling
├── pdf-preamble.tex     # PDF/LaTeX styling
├── fonts/               # Embedded TeX Gyre Pagella fonts
├── Cover.png            # Book cover (KDP spec: 1600 × 2560 px)
├── generate_cover.py    # Cover generation script
├── kdp-metadata.md      # Amazon KDP submission guide
└── _book/               # Rendered output (gitignored)
```

---

## Building the Book Locally

You will need [Quarto](https://quarto.org/docs/get-started/) installed.

```bash
# Clone the repository
git clone https://github.com/gloria-aiyebogun/Rebuilding-After-the-Shatter.git
cd Rebuilding-After-the-Shatter

# Render all formats (HTML, PDF, EPUB)
quarto render

# Publish to GitHub Pages
quarto publish gh-pages
```

---

## License

© 2026 Gloria Ichoja Aiyebogun. All rights reserved.

The text of this book is made freely available for personal reading via GitHub Pages. It may not be reproduced, distributed, or sold without the written permission of the author.
