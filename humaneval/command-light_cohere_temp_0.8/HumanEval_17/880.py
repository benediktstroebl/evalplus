```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, ".":": 1,
        ".":": 1,
        ".";": 1,
        "oO": [4, 2],
        "oo": [2, 2],
        "ooo": [1, 4],
        # ... and so on
    }
    return [notes[note] for note in music_string.from(music_string)]

def test_parse_music():
    music_str = "ooO .| O o| .| .| .| .| .| oO"
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert expected == actual
```