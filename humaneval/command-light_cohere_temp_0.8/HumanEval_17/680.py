```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes.get(note) for note in music_string.make_tuple() if note not in notes]

def test_parse_music():
    music_str = 'o o| .| o| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert expected == actual
```