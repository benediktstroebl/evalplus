```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.': 1,
    }
    return [notes[c] for c in music_string.

# Test cases
print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('|.o .| .o'))  # [1]
print(parse_music('o o.'))  # [4, 4] (invalid input, should return an error)
```