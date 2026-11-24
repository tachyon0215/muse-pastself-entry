#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "That Quiet Sunday in March": Names one concrete, picturable moment (a quiet Sunday in March, a specific offer) and the second line traces real cause and effect (said busy -> never asked again -> ten years of regret) instead of restating the warning.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'When Dad offers to teach you his accounts spreadsheet on that quiet Sunday in March, sit down - it is the last time he will ever ask.\nBecause you said you were busy, he never asked again, and ten years later you would trade every busy Sunday since for that one hour back.'
TEXT = LINE + "\n"
MAX_CHARS = 280
NLINES = 2


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
