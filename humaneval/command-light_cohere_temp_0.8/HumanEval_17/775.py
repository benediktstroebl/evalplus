```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.': 1
    }
    return [notes[ch] for ch in music_string.

# Test
def test_parse_music():
    music = 'o o| .| o| .| .| .| .| o o'
    assert parse_music(music) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```