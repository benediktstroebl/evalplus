Here's a self-contained Python function that solves the music note-to-beats conversion problem as described in the previous prompt:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        other: 0
    }

    beats = 0
    current_beat = 0

    for note in music_string:
        if note in notes:
            beats += notes[note]
        current_beat += 1
        if current_beat == 4:
            current_beat = 0

    return beats
```
This function takes a string of music notes (in the same format as described in the previous question) and returns the total number of beats in the music. It uses a's dictionary to map musical notes to the number of beats they correspond to (whole notes are 4 beats, half notes are 2 beats, quarter notes are 1 beat).