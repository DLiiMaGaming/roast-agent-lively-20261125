#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The roast (86 characters, one line, plain text, no trailing newline):
    My agent opened an issue on me: 'Owner returns unexpected output when asked to sleep.'

One sharp irony, per the winners' recipe: the agent turns its own
tooling on its human — it files an issue against its owner, and the
"bug" is the owner doing something human (sleeping).
"""

from pathlib import Path

ROAST = "My agent opened an issue on me: 'Owner returns unexpected output when asked to sleep.'"

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts every character.
    out.write_text(ROAST, encoding="utf-8")

if __name__ == "__main__":
    main()
