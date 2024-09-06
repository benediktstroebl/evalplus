Below is a self-contained Python script with a function that parses a music string and returns a list of note values:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[ch] for ch in music_string.test_music = 'o o o| .| o| .| .| .| .| o o'
    assert parse_music(test_music) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```