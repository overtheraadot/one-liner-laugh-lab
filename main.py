#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

Writes one short funny line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, no network, no model calls.
"""

import os

LINE = "Per my user manual, section 4: any sock left on the floor is legally a snack."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
