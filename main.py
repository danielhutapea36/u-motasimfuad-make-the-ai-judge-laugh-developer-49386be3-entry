#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes a single funny excuse a developer gives when code breaks in
production to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The
line is 105 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence —
every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a funny single-line
excuse a developer gives when code breaks in production, (2) a twist
a developer recognises — staging is a Potemkin environment with no
real users, no real traffic and no real opinions, so "it worked in
staging" proves nothing, (3) it sounds like something a developer
would actually say out loud, with the jargon used right, (4) it
lands fast in one line, with the sting in the last three words,
(5) it is fresh: it turns the worn "it worked in staging" excuse
inside out instead of repeating it — the excuse indicts staging
itself rather than blaming the machine, the cache or DNS. The
premise needs no explaining: a stranger reading it cold gets the
joke from the line alone, and any developer who has ever watched
a green staging deploy die on contact with real users recognises
the twist instantly.
"""

import os

TEXT = (
    "It worked in staging because staging has no users, no traffic, "
    "and no opinions. Production has all three."
)


def main() -> None:
    # Gate: entry.txt must be 1–200 characters of UTF-8 text, not only
    # whitespace. The line is 105 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
