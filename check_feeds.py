#!/usr/bin/env python3
"""Prova tots els feeds de feeds.json i diu quins funcionen.

Executa-ho una vegada abans de començar:  python check_feeds.py
Substitueix a feeds.json els que surtin amb ERROR.
"""
import json
from pathlib import Path

import feedparser
import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; NoticiesJove/1.0)"}
config = json.loads((Path(__file__).parent / "feeds.json").read_text("utf-8"))

for cat_id, cat in config["categories"].items():
    print(f"\n{cat['nom']}")
    for f in cat["feeds"]:
        try:
            r = requests.get(f["url"], headers=HEADERS, timeout=20)
            r.raise_for_status()
            n = len(feedparser.parse(r.content).entries)
            estat = f"OK ({n} notícies)" if n else "ERROR (feed buit o no és RSS)"
        except Exception as exc:
            estat = f"ERROR ({exc.__class__.__name__})"
        print(f"  {f['source']:<14} {estat:<32} {f['url']}")
