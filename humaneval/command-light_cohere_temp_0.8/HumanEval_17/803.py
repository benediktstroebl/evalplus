```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beat = 1
    notes_list = []
    for note in music_string.split(' '|'):
        note = note.split('o supports: 'o')
        note = int(note)
        notes_list.append(note)
    beat += 1
    return notes_list
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert actual == expected
    music_str = ' .o .o| .| o'
    expected = [1, 2]
    actual = parse_music(music_str)
    assert actual == expected
```