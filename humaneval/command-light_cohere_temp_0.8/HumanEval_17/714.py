Here's a self-contained Python function that solves the music-notes-to-beats problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }

    beats = [notes[note] for note in music_string.tap music_string if in notes.

    return beats
 beats
```

This solution defines a dictionary that maps music notes to the number of beats that each represents. 

The function then loops through each unique note in the music_string, and returns the number of beats for that note.

This solution ensures the code is self-contained and doesn't rely on any external classes, modules or functions. 

Note that this solution can be easily tested by providing various input music_strings and checking if the returned beat numbers are correct.