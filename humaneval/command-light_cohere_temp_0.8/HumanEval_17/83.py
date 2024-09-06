Here's a self-contained Python function that takes a music string and returns a list of integers, each representing the number of beats of a note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        other: None
    }

    beats = 0

    for note in music_string.get():
       
        note:
        if note.isalpha():
            key = next(notes.get(note),
            beats += notes[key])

    return list(beats)
``` 
This function uses a dictionary `notes` to map musical notes to the number of beats each note lasts. The function iterates through the string and increment the beat count for each encountered note, and finally returns a list of these beat counts.