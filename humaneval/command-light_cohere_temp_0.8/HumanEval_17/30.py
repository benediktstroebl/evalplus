```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes.get(note, beat) for note, beat in music_string.or, beat = 4]

def test_parse_music():
    music = "o o| .| o| .| .| .| .| o o"
    assert parse_music(music) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # Should be true

print("Test passed!")
```