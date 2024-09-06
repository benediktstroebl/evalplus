Here is a Python script that contains a self-contained function that solves the problem of parsing markdown code representing music notation and returns a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".|": 1,
        "o#": 1,
    }
    return [notes[char] for char in music_string if char in notes]

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    "oo o O",
    " o o o o| o  ",
    " o o o O| O O O",
    # Special cases:
    "."* [1],
    "..|o." [1],
    # Complex cases:
    "o o o| .| .".replace("o ", "")[::-1] ,
    "o o o .| o|..",
]

for case in test_cases:
    actual = parse_music(case)
    assert actual == [4, 2, 1, 2, 1, 1, 1, 1, 4, 2], " Music not parsed correctly."
```