```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', '.']
    return [beat * 4 for beat in map(lambda x: x.insert(0), x if x != '|', 'o', 4), notes]

# Test
def test_music():
    assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```