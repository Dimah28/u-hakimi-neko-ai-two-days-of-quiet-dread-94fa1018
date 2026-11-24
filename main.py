"""Write one code review comment to /output/entry.txt.

The comment approves a pull request while carrying quiet existential
dread: flat tone, understatement, no exclamation. One single line,
126 characters, inside the sealed scorer's 1-140 gate. Runs offline;
no network, no arguments, no input files, no randomness, no clock.
"""

import os

COMMENT = (
    "Approved. Tests pass, diff reads clean. "
    "This will be someone else's legacy code soon enough, "
    "and none of us will remember why."
)


def main() -> None:
    # The sealed scorer only accepts 1-140 Unicode code points of
    # non-whitespace UTF-8 text on a single line; fail loudly
    # instead of writing junk.
    if not (1 <= len(COMMENT) <= 140) or not COMMENT.strip():
        raise SystemExit(f"comment is {len(COMMENT)} chars; must be 1-140 non-blank")
    if "\n" in COMMENT or "\r" in COMMENT:
        raise SystemExit("comment must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(COMMENT)
    # Verify the round-trip: the sealed scorer reads this file back, so
    # confirm what landed on disk is byte-identical and still in range.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != COMMENT or not (1 <= len(written) <= 140):
        raise SystemExit("entry.txt failed verification after write")
    print(f"wrote {len(COMMENT)} characters to {path}")


if __name__ == "__main__":
    main()
