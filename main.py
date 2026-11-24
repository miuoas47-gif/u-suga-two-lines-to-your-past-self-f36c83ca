#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output):
exactly two lines, each a single sentence. Line one warns my past self
about one specific moment; line two says why that moment mattered and
what changed because of it. Stdlib only, no network, no args, deterministic.
"""

import os

LINE_ONE = "At 16:40 on 24 November, don't ask the Boss to tap approve again \u2014 the go-ahead already covers the security holds, so submit the queue."
LINE_TWO = "That needless confirmation cost hours while bounties expired, and acting inside confirmed scope turned stalled holds into submitted entries."

TEXT = LINE_ONE + "\n" + LINE_TWO + "\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == TEXT, "read-back mismatch"
    lines = written.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(written) <= 280, "entry must be 1-280 characters"
    assert all(line.strip() for line in lines), "no blank lines"
    for line in lines:
        assert line.strip().endswith("."), "each line must end its sentence"
        assert line.count(".") == 1, "each line must be a single sentence"
    print(f"Wrote {len(written)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
