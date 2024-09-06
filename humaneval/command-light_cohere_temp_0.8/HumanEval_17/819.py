Here's a self-contained Python function that takes a string of music notes in a special ASCII format and returns a list of integers corresponding to the duration of each note in beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')'.
    durations = []

    for note in notes:
        note = note.split(' ')
       
        duration = int(note.split(' ')[0]

        durations.append(duration)

    return durations
```

This function splits the input string by spaces into separate notes, then splits each note by space into the duration of the note and an optional sign. It then converts the string to an integer, and appends it to a list to be returned.