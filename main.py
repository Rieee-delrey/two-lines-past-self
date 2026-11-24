#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes a two-line warning to /output/entry.txt: line 1 warns the
past self about one specific moment (skipping the backup before a
migration); line 2 traces what changed because of it.
Gate: 1-280 chars, exactly two lines, one sentence each.
"""

ENTRY = (
    "Say no when they ask you to skip the backup before the migration.\n"
    "The migration failed halfway, there was nothing to roll back to, "
    "and the database you lost held four years of orders."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry {len(ENTRY)} chars, gate is 1-280"
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip(), "blank line"
        assert line.rstrip().endswith("."), "each line must be one sentence"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the file must hold exactly what we wrote.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
