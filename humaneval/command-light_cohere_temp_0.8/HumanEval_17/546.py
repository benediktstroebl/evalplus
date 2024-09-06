Here's a self-contained Python function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "..": 4,
        "."": 1
    }
    return [notes[char] for char in music_string.test_music = "o o| .| o| .| .| .| .| o o"
    assert parse_music(test_music) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This function, 'parse_music', takes a string music_string as input and creates a list of integers representing the number of beats that each character in the string represents.  The provided legend, the function maps the characters 'o', 'o|', '.|', 'o', '.' and '.' to their respective beat values.