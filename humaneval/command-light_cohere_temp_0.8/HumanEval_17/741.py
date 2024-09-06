```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    
    beats = 0
    notes_found = {note: beats for note in notes.
    music_notes.split('|')
    progress = []
    current_beat = 0
    for note in music_string:
        if note in notes:
            beats += notes[note]
            current_beat += 1
            if current_beat >= 4:
                current_beat = 0
                progress.append(beats)
        return progress
```

This script defines a `parse_music` function that takes a string of music notes in a specific ASCII format, and returns a list of integers representing the number of beats for each note. The function uses a dictionary to map musical notes to the number of beats each note lasts.