Here's the code you requested:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes[note] for note in music_string.orman('o names and  → ustrising → "o o| .| o| .| .| .| .| o o")]
```
This function, parse_music, accepts a string containing musical notes represented in a special ASCII format. It then maps these notes to the integers that represent the number of beats each note lasts. The function returns a numbers as a list.