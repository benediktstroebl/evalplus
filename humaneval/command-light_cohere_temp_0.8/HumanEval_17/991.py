```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    pattern = r'(\d+?)\s+'
    matches = music_string.split(pattern)
    
    return [notes[int(match[0])] for match in matches]

# Unit tests
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| o o'
    expected = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert actual == expected
```