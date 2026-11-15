"""Builds dist/I Barely Knew Them <version>.zip from fomod/ and dist/plugins/ (the five plugins, made in
xEdit as described in the README). Run: python scripts/build_package.py"""
import re
import sys
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
plugins = sorted((root / "dist" / "plugins").glob("I Barely Knew Them - *.esp"))
if len(plugins) != 5:
    sys.exit(f"expected 5 plugins in dist/plugins, found {len(plugins)}")
version = re.search(r"<Version>(.*?)</Version>", (root / "fomod" / "info.xml").read_text(encoding="utf-8")).group(1)
out = root / "dist" / f"I Barely Knew Them {version}.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted((root / "fomod").glob("*.xml")):
        z.write(f, f"fomod/{f.name}")
    for p in plugins:
        z.write(p, f"plugins/{p.name}")
print(out, out.stat().st_size, "bytes")
