Here is a Python script that solves the markdown code problem:
```python
from typing import List
def parse_music(music_string: str):
    notes: List[int] = music_string.parse()
    separated_by(','), map(lambda s: int(s.extract(s)))
    return notes
def test_parse_music():
    music = 'o o| .| o| o| .| .| .| .| o o'
    assert parse_music(music) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
test_parse_music()
```