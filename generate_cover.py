"""
Cover generator for "Rebuilding after the Shatter"
KDP ebook cover: 1,600 x 2,560 px (1:1.6 portrait ratio, 300 DPI)
"""

from PIL import Image, ImageDraw, ImageFont

# ── Dimensions ────────────────────────────────────────────
W, H = 1600, 2560

# ── Colour palette ────────────────────────────────────────
BG_TOP    = (22, 14, 42)    # Very deep plum
BG_BOTTOM = (48, 26, 66)    # Slightly lighter plum
CREAM     = (245, 232, 205) # Warm cream — title & author
GOLD      = (195, 158, 100) # Warm gold — rules & accents
DIM_CREAM = (180, 165, 143) # Muted cream — subtitle & quote

FONT_DIR  = "fonts/"

# ── Load fonts ────────────────────────────────────────────
title_font    = ImageFont.truetype(FONT_DIR + "texgyrepagella-bold.otf",       152)
subtitle_font = ImageFont.truetype(FONT_DIR + "texgyrepagella-italic.otf",      50)
author_font   = ImageFont.truetype(FONT_DIR + "texgyrepagella-regular.otf",     62)
label_font    = ImageFont.truetype(FONT_DIR + "texgyrepagella-italic.otf",      36)
quote_font    = ImageFont.truetype(FONT_DIR + "texgyrepagella-italic.otf",      58)

# ── Create image with vertical gradient ───────────────────
img = Image.new("RGB", (W, H), BG_TOP)
draw = ImageDraw.Draw(img)

for y in range(H):
    ratio = y / H
    r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * ratio)
    g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * ratio)
    b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * ratio)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# ── Helpers ───────────────────────────────────────────────
def text_height(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[3] - bb[1]

def draw_centered(draw, text, y, font, color):
    bb = draw.textbbox((0, 0), text, font=font)
    x = (W - (bb[2] - bb[0])) // 2
    draw.text((x, y), text, font=font, fill=color)
    return bb[3] - bb[1]

def draw_rule(draw, y, width_frac=0.30, color=GOLD, thickness=2):
    rw = int(W * width_frac)
    x0 = (W - rw) // 2
    draw.rectangle([(x0, y), (x0 + rw, y + thickness)], fill=color)

# ─────────────────────────────────────────────────────────
# LAYOUT
# ─────────────────────────────────────────────────────────

# ── Title block ───────────────────────────────────────────
y = 620
y += draw_centered(draw, "Rebuilding", y, title_font, CREAM) + 12
y += draw_centered(draw, "after the",  y, title_font, CREAM) + 12
y += draw_centered(draw, "Shatter",    y, title_font, CREAM) + 40

# ── Rule below title ──────────────────────────────────────
draw_rule(draw, y, width_frac=0.32)
y += 60

# ── Subtitle ──────────────────────────────────────────────
sub_lines = [
    "A Woman's Guide to Healing from Heartbreak,",
    "Reclaiming Her Worth, and Living in",
    "Emotional Freedom",
]
for line in sub_lines:
    y += draw_centered(draw, line, y, subtitle_font, DIM_CREAM) + 18
y += 60

# ── Double rule separator ─────────────────────────────────
draw_rule(draw, y,     width_frac=0.50, color=GOLD, thickness=1)
draw_rule(draw, y + 8, width_frac=0.50, color=GOLD, thickness=1)
y += 80

# ── Pull quote ────────────────────────────────────────────
quote_lines = [
    "\u201cYou are not broken.",
    "You are becoming.\u201d",
]
for line in quote_lines:
    y += draw_centered(draw, line, y, quote_font, DIM_CREAM) + 16
y += 60

# ── Double rule separator ─────────────────────────────────
draw_rule(draw, y,     width_frac=0.50, color=GOLD, thickness=1)
draw_rule(draw, y + 8, width_frac=0.50, color=GOLD, thickness=1)

# ── Author name (bottom, anchored) ────────────────────────
draw_rule(draw, 2340, width_frac=0.50)
draw_centered(draw, "Gloria Aiyebogun", 2378, author_font, CREAM)
draw_rule(draw, 2468, width_frac=0.50)

# ── Save ─────────────────────────────────────────────────
out = "Cover.png"
img.save(out, "PNG", dpi=(300, 300))
print(f"Saved: {out}  ({W} x {H} px)")
