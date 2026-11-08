#!/usr/bin/env python3
"""يولّد index.html بتاع تطبيق الأدمن من index.html بتاع موقع رقيب.
الاستخدام:  python3 tools/build.py /path/to/Maroo/index.html"""
import re, sys, pathlib
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../Maroo/index.html")
root = pathlib.Path(__file__).resolve().parent.parent
s = src.read_text(encoding="utf-8")

def sub(pat, rep, flags=0, count=0):
    global s
    s, n = re.subn(pat, rep, s, count=count, flags=flags); return n

HIDE = ('<style>body>*:not(#ad2):not(#ib):not(script):not(style){display:none!important}</style>')
assert sub(r"<head>", '<head><meta name="robots" content="noindex,nofollow"><script>window.RQ_ADMIN=1</script>' + HIDE, re.I, 1) == 1
sub(r"<meta name=\"description\"[^>]*>", "")
sub(r"<meta property=\"og:[^>]*>", "")
sub(r"<meta name=\"twitter:[^>]*>", "")
sub(r"<link rel=\"canonical\"[^>]*>", "")
sub(r"<script type=\"application/ld\+json\">.*?</script>", "", re.S)
s = s.replace("<title>رقيب | تركيب وصيانة كاميرات المراقبة</title>", "<title>رقيب — الأدمن</title>")
s = s.replace('<meta name="theme-color" content="#12263A">', '<meta name="theme-color" content="#0A1626">')
s = s.replace('<meta name="apple-mobile-web-app-title" content="رقيب">', '<meta name="apple-mobile-web-app-title" content="أدمن رقيب">')
s = s.replace("admin-icon-192.png", "icon-192.png")
# شاشة تحميل بدل ما موقع رقيب يظهر لحد ما الأدمن يفتح
assert s.count('<div id="ad2"></div>') == 1
s = s.replace('<div id="ad2"></div>', '<div id="ad2" class="on"><p style="text-align:center;margin-top:30vh;color:var(--mut)">جاري التحميل…</p></div>')
(root / "index.html").write_text(s, encoding="utf-8")
print("index.html", len(s), "bytes")
