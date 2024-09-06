```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' ')
   ator that music_string.
    return [output: [int(beat) for beat in beats.
def test_music() -> None:
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4], "Pass failed"
    assert parse_music('oo .| .o| .') == [1, 2, 4, 1, 2], "Pass failed"
    assert parse_music('o o o .') == [4, 4, 1, 1], "Pass failed"
    assert parse_music('.).o .| .|') == [1, 1], "Pass failed"
    assert parse_music('') == [], "Pass failed"
    return None
```