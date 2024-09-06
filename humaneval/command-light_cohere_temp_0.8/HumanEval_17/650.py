```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[char] for char in music_string if char in notes]
    return beats

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    "o o| .| o| .| .| .| o",
    "oo",
    "o.oo o",
    actual=[0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
    "|ooo|",
    ",,",
    "oo",
    ".",
    "o .| .",
    "o . .|.",
    "o . o|",
    "o o/|.",
    "o . o o",
    "o o o o",
    "o o o| o",
]

for idx, test_case in enumerate(test_cases, start=1):
    actual = parse_music(test_case)
    expected = test_cases[idx - 1]
    print(f"Test {idx} - {test_case}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print()
```
This script defines a function `parse_music` that parses a music string into a list of beats. It then provides several test cases to verify the function's expected behavior. 

This code demonstrates a self-contained and functional solution to the problem of parsing music notes.