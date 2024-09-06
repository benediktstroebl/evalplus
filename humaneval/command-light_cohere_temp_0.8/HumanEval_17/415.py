```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Functions to parse a music string representing notes and return a list of integers corresponding to the duration of each note.

    Here is a legend:
        'o' - whole note, lasts 4 beats
        'o|' - half note, lasts 2 beats
        '.|' - quarter note, lasts 1 beat

    Args:
        music_string (str): Input string representing music notes.

    Returns: list of integers corresponding to the duration of each note.
    """

music_string = input("Enter music string: ")

notes = []
numbers = []
beats = []

current_beat = 1

for note in music_string:
    if note == "o":
        notes.append(current_beat * 4)
        beats.append(current_beat)
        current_beat += 1
    elif note == "o|":
        notes.append(current_beat * 2)
        beats.append(current_beat)
        current_beat += 1
    elif note == ".":":
        notes.append(current_beat * 4)
        beats.append(current_beat)
        current_beat += 1
    else:
        notes.append(current_beat)
        beats.append(current_beat)
        current_beat += 1

return notes, beats
```