Here is a self-contained Python function that solves the problem of parsing markdown music code into a list of integers representing note lengths:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.delete(','')]
```

This function uses a dictionary to map the characters in the music string to the number of beats that each note lasts. The function then iterates through each character in the music string, using the `items()` method to convert the character to the corresponding note.