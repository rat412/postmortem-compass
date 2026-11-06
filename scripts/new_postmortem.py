#!/usr/bin/env python3
"""Scaffold a new postmortem file from the template. Stdlib only.

Usage:
    python3 new_postmortem.py --title "Payment API outage" --sev SEV2 --date 2026-11-06
    python3 new_postmortem.py --title "DB failover" --sev SEV1 --out ./reports
"""
import argparse
import datetime
import pathlib
import re
import sys

TEMPLATE = pathlib.Path(__file__).resolve().parent.parent / "templates" / "postmortem-template.md"
VALID_SEV = {"SEV0", "SEV1", "SEV2", "SEV3", "SEV4"}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9一-鿿]+", "-", text)
    return text.strip("-") or "incident"


def main() -> int:
    ap = argparse.ArgumentParser(description="Create a new postmortem from the template.")
    ap.add_argument("--title", required=True, help="Incident title")
    ap.add_argument("--sev", default="SEV2", help="Severity: SEV0-SEV4 (default SEV2)")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="YYYY-MM-DD")
    ap.add_argument("--tz", default="UTC+8", help="Reference timezone (default UTC+8)")
    ap.add_argument("--out", default=".", help="Output directory")
    args = ap.parse_args()

    sev = args.sev.upper()
    if sev not in VALID_SEV:
        print(f"error: --sev must be one of {sorted(VALID_SEV)}", file=sys.stderr)
        return 2
    try:
        datetime.date.fromisoformat(args.date)
    except ValueError:
        print("error: --date must be YYYY-MM-DD", file=sys.stderr)
        return 2

    body = TEMPLATE.read_text(encoding="utf-8")
    body = (body.replace("{TITLE}", args.title)
                .replace("{DATE}", args.date)
                .replace("{SEV}", sev)
                .replace("{TIMEZONE}", args.tz))

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"postmortem-{args.date}-{slugify(args.title)}.md"
    if path.exists():
        print(f"error: {path} already exists", file=sys.stderr)
        return 1
    path.write_text(body, encoding="utf-8")
    print(f"created: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
