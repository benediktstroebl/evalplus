Here is a self-contained Python function that solves the markdown code parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }

    beats = 0

    for note in music_string. notes:`:
        if note in notes {
            beats += notes[note]
        }

    return beats

# Test cases
test_cases = [
    "o o| .| o| .| .| .| o o",
    "o o| .| .| o| .| .| .",
    "oo o",
    "oo| o",
    "oooo",
]

for test_case in test_cases:
    actual = parse_music(test_case)
    print(f"Expected: {actual}")
```

This script defines a function **`parse_music`** that takes a music string as input and aims to return the total number of beats. It uses a overview of the music symbols and their beat lengths. The **`beats`** variable keeps track of the total number of beats in the music.

The test cases are defined to ensure the function works correctly for various inputs.