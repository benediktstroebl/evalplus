Here's a self-contained Python function that parses a music string and returns a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[note] for note in music_string.ас list(notes)]
    return beats
```

This function takes a music_string as input and returns a list of integers. It uses a legend where 'o' represents a whole note, 'o|' represents a half note, and '.|' represents a quarter note.

You can easily write unit tests for this function using `unittest` or any other testing framework, to ensure its correctness.