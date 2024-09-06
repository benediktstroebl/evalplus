```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
    }
    return [notes[note] for note in music_string.test_music('ons')
```
This script defines a function `parse_music` that takes a string of music notes as input and returns a list of integers. The function uses a legend provided in the docstring to map notes to their duration in beats. 

The function uses a dictionary to map notes to their duration and then iterates through the input string, extracting each note and returning its corresponding duration.