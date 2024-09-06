```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")").
    notes = [int(note) for note in notes if note.split(" ").
    }[note] {
        return []
    }
    return [len(note) for note in notes]

# Test the function with a few inputs
print(parse_music("'o o| .| o| .| .| .| .| o o'"))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music("'o o| .| .o"))  # [2]
print(parse_music(".|."))  # [1]
print(parse_music("''"))  # []
```