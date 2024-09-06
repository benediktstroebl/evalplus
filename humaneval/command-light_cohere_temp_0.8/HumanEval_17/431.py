```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    pattern = r'([^'o'|.|']{4})'
    return [int(x) for x in re.search(pattern, music_string)]
def test_music_parser():
    music = 'o o| .| o| .| .| .| o o'
    assert parse_music(music) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
```