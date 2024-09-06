```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
    }
    return [notes[note] for note in music_string.test_music = [
        music_string + '\n' + 'o o| .| o| .| .| .| .| o o']
    assert parse_music(test_music) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```