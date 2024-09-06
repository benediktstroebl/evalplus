```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = [notes[ch] for ch in music_string.split(' '|')]
    
    return beats
```
This Python function named `parse_music` takes a string `music_string` as input and aims to parse the music notes represented in that string into a list of integers. It uses a legend to interpret the special characters as different note values. The function is designed to be self-contained and pass all corresponding tests.