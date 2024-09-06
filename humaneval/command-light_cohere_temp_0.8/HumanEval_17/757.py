Here's a self-contained Python function that successfully parses markdown musical code into a list of note durations:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.
``` 
This function uses a dictionary to map musical note characters to their respective durations. The function is then iterates over the input music string, and returns a list of corresponding durations.