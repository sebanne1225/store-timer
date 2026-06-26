# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import os
OUT = os.path.dirname(os.path.abspath(__file__))

def icon(size):
    img = Image.new("RGB", (size, size), (15, 20, 25))   # dark bg
    d = ImageDraw.Draw(img)
    cx = cy = size // 2
    r = int(size * 0.34)
    w = max(2, size // 28)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(74, 158, 255), width=w)  # clock face
    d.line([cx, cy, cx, cy - int(r * 0.62)], fill=(74, 158, 255), width=w)         # hour hand
    d.line([cx, cy, cx + int(r * 0.5), cy + int(r * 0.12)], fill=(46, 204, 113), width=w)  # minute hand
    rr = max(3, size // 36)
    d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(255, 255, 255))          # center dot
    img.save(os.path.join(OUT, f"icon-{size}.png"))

icon(192)
icon(512)
print("icons done")
