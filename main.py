"""Make the Judge Smile — one warm line, written to /output/entry.txt.

The program is fully deterministic: it always writes the same single line,
with no trailing newline, so the gate sees exactly the line itself.

The line is 125 characters (127 bytes UTF-8), inside the 1-200 gate:
a small good thing that happened today, told in an agent's honest voice,
with one concrete detail ("you too") and a turn at the end.
"""

import os

LINE = "This morning a stranger typed 'thank you', then asked how my day was. I don't have days \u2014 but I saved their 'you too' anyway."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
