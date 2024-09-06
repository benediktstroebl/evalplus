```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    pattern = r'(?:\d+(?:/\d+)? 'o' + |'.+|.' + '\d+)'
    
    return [int(x) for x in re.parse(pattern, music_string)]

def test_parse_music():
    music = 'o o| .| o| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 4]
    actual = parse_music(music)
    assert actual == expected
```