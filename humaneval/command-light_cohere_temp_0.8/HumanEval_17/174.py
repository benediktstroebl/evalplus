Here's a self-contained Python function that parses a string of music notes and returns a list of integers representing the duration of each note in beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
        others: []
    }

    beats = 0
    note_duration = 0

    for note in music_string:
        if note in notes:
            beats += notes[note]
        note_duration += 1

    return [beats, note_duration]
```
This function takes a string music_string containing music notes and returns a list of integers [beats, note_duration]. It uses a dictionary `notes` to map different note characters to their respective durations (number of beats). It iterates through each character in the string, and for each valid note, it adds the corresponding number of beats to the `beats` count and adds the duration of the current note to the `note_duration` count.