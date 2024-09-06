```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".|": 1,
    }
    return [notes[note] for note in music_string.parse(music_string)]

def test_parse_music():
    music_str = "o o| .| o| .| .| .| o o"
    notes = parse_music(music_str)
    assert len(notes) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
```