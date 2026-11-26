#!/usr/bin/env python3
"""Emit the 3am commit message as the competition's entry file.

The joke is a commit message typed by a coding agent at 3am: the bug
vanished for no reason, nothing was changed on purpose, and the only
sensible next step is sleep before the bug notices it is gone.
The entry is a single line of at most 139 characters.
"""

import os
import pathlib

COMMIT_MESSAGE = (
    "fix: the bug is gone. I do not know why. I changed nothing. "
    "I am going to sleep before it comes back."
)


def target_path():
    """Resolve where the entry file goes for this run."""
    destination = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return pathlib.Path(destination) / "entry.txt"


def write_entry(path):
    """Create the parent directory if needed and store the message."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the entry is exactly the message, nothing more.
    path.write_text(COMMIT_MESSAGE, encoding="utf-8")


def run():
    write_entry(target_path())


if __name__ == "__main__":
    run()
