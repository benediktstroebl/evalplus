Here is a self-contained Python function that solves the problem you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".";": 1
    }
    return [notes[note] for note in music_string.ly]
```
This function takes a string of music notes represented in a special ASCII format and parses it into a list of integers representing how many beats does each note last.