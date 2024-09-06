```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        '.': 1
    }
    return [notes[char] for char in music_string.

# Test
def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    assert parse_music('o o| .| .o') == [4, 2]
    assert parse_music('|o o| .| .o') == [1, 4, 2]
    assert parse_music(''). == []
```