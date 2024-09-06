```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        "..." : 4,
        "o o": 8  # Test case
    }
    return [notes[note] for note in music_string.test_music = [parse_music('o o| .| o| .| .| .| .| o o')] and all(test_music) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]]
```