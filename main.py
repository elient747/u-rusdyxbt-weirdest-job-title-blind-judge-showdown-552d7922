#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — one original job title,
1 to 60 characters, the weirdest one we could think of.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single title to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the title is built inside write_entry(); entry.txt mirrors it
# exactly. (Rev 2: kept the corporate "Senior ... for ..." frame — it
# sounds like a real job, and the twist is that the cars need apologies.)
import os


def write_entry():
    line = "Senior Apologizer for Self-Driving Cars"
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
