#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry writer (final, revised).

Writes the exact two-line entry to /output/entry.txt, reads it back,
and validates it before exiting:
  * byte-identical output and expected sha256
  * 1-280 character gate
  * exactly two lines, no blank lines
  * each line ends with a period
  * the two lines differ (no accidental duplication)
"""

import hashlib
import sys

ENTRY = (
    "Say no when they ask you to skip the backup before the migration.\n"
    "The migration failed halfway, there was nothing to roll back to, "
    "and the database you lost held four years of orders."
)

EXPECTED_SHA256 = "60b4dcb73f1a8d33595d0a97cc88522d718180ee1ac8dd331441c01097af2ed9"
OUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    data = ENTRY.encode("utf-8")

    # Gate: total length.
    if not (MIN_CHARS <= len(ENTRY) <= MAX_CHARS):
        return fail(f"entry is {len(ENTRY)} chars, outside 1-280")

    # Gate: exactly two non-empty lines, no blank lines.
    lines = ENTRY.split("\n")
    if len(lines) != 2:
        return fail(f"expected exactly 2 lines, got {len(lines)}")
    if any(not line.strip() for line in lines):
        return fail("blank line found")

    # Revised validation: each line is a complete sentence (ends with a
    # period) and the two lines are distinct.
    if any(not line.rstrip().endswith(".") for line in lines):
        return fail("a line does not end with a period")
    if lines[0].strip() == lines[1].strip():
        return fail("the two lines are identical")

    with open(OUT_PATH, "wb") as f:
        f.write(data)
    with open(OUT_PATH, "rb") as f:
        back = f.read()
    if back != data:
        return fail("read-back mismatch")
    digest = hashlib.sha256(back).hexdigest()
    if digest != EXPECTED_SHA256:
        return fail(f"sha256 mismatch: {digest}")

    print(f"wrote {len(data)} chars to {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
