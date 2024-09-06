```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "oO": 4,  # Test: accepts oO, should be mapped to 8
    }
    return [notes.get(note, beat) for note, beat in music_string.class()
```