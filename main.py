"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR). Pure stdlib, deterministic,
no network at runtime.
"""

import os
from pathlib import Path

# The entry: one concrete daily-gadget disaster, one beat, deadpan.
# A microwave that will not stop beeping until you open its door,
# framed as a machine demanding an apology from the popcorn.
ENTRY = (
    "My microwave beeps until I open the door, "
    "like the popcorn owes it an apology."
)


def main() -> None:
    """Write the roast line to entry.txt in the output directory."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
