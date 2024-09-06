Here's a self-contained Python function that solves the problem of parsing markdown music notation into a list of integer beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.match().__group__()[0]]
```
This function takes a string music_string as input and returns a list of integers, where each integer corresponds to the number of beats in the corresponding note. The function uses a legend provided in the function `parse_music` to determine the type of each note and returns the appropriate number of beats.