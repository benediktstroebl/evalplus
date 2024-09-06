```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, ".":": 1,
        ".";": 1, "oO": 4, "oO|": 2, "OO|": 1,
    }
    return [notes[c] for c in music_string.

# Test cases
test_music1 = "o o| .| o| .| .| .| o o"
test_music2 = "."; .|. "oo"
test_music3 = "|/-/|"  # One whole note, four beats long, with emphasis

print(parse_music(test_music1))  # Output should be [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
print(parse_music(test_music2))  # Output should be []
print(parse_music(test_music3))  # Output should be [1]
```