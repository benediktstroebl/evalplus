Here is a self-contained Python function that solves the problem of converting a music string into a list of integers representing note durations:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = [notes[note] for note in music_string.map(setdefault=notes)
    return beats
```

This function utilizes a dictionary to map musical notes to their respective durations. It then iterates through each character in the input string to find the corresponding note duration.