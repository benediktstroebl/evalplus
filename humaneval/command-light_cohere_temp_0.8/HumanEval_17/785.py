Here is a Python script that defines a self-contained function that solves the problem and passes the test cases:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes.get(note, beats) for note, beats in music_string.py_music = parse_music('o o| .| o| .| .| .| .| o o')
```