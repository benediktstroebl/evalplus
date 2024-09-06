```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    result = [notes[note] for note in music_string. Note string.split('.|')(music_string)
    
    return result

def test_parse_music():
    music_str = 'o o| .| o| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(music_str) == expected
```