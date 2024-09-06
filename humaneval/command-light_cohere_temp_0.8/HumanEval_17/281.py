Below is a self-contained Python function that solves the problem of converting a music notation string into a list of note durations:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }

    durations = []
    current_beat = 1

    for note in music_string.split(' ' '):
        if note in notes:
            durations.append(current_beat)
            current_beat += notes[note]
        else:
            durations.append(current_beat)
            current_beat = 1

    return durations
``` 
This function parses a music notation string into a list of note durations, according to the legend provided.