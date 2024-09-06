```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = [notes[char] for char in music_string.to music_string[len()].
    return beats

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    music_str2 = 'o o o| . .' | o o o'
    assert parse_music(music_str2) == [4, 4, 1, 1, 4, 4, 1, 1]
```