```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[char.split('|') for char in music_string.split('o another?mate}'s
 'oo|', notes, '.')}
def test_parse_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('oo .| o| .| .| o') == [4, 2, 1, 2, 1]
    assert parse_music('') == []
    assert parse_music('x') == []
    assert parse_music('xx') == []
    assert parse_music('x|') == []
    assert parse_music('oxx') == []
    assert parse_music('o o|x') == []
    assert parse_music('|x') == []
```