```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes.get(note) for note in music_string.parse(''.

# Tests
def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o o| .| .| .| .| .') == [4, 4, 1, 2, 2, 1, 1, 1, 1, 1]
    assert parse_music('.' == [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert parse_music('this is not valid') == []
```