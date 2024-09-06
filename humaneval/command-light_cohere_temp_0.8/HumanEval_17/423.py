```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        ".":o": 4,
        "|": 1
    }
    return [notes[note] for note in music_string.test_music_parse_music("oo o o| .| o| .| .| .| .| o o")]
```