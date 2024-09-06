```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beats = [notes.get(x, notes.a., notes.get('.ound), a other notes, 4]

    notes_list = []
    for beat in beats:
        for note in music_string:
            if note in notes:
                notes_list.append(beat * (notes[note] // beat))
                break
        notes_list.append(beat)

    return notes_list
``` 
This script defines a function **`parse_music`** that takes a music string as input and returns a list of integers representing the number of beats in the music. It uses a legend of whole notes, half notes, and quarter notes, where each note is equivalent to 4 beats. The function iterates through each beat and each character in the music string to fill the list of beats and appends the beat to the notes list.