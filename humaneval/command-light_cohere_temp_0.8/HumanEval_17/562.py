Here is a self-contained Python function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.HS]
```
This function takes a string of music represented in the same format as in the previous problem, and returns a list of integers. It uses a format string to map each note to the number of beats it lasts.