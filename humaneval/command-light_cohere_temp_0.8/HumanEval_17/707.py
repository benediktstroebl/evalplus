```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[char.get(0)] for char in music_string if char.isalpha()]

def test_parse_music():
    test_data = ['o o| .| o| .| .| .| o o', 'o o| .', 'o|,.','.center('o')] + ['o', 'o|', '.', '.'] * 4
    expected = [4, 2, 1, 2, 1, 2, 4, 4, 4]
    assert parse_music(test_data) == expected
```