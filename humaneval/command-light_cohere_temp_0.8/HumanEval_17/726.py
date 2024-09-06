Here's a self-contained Python function that parses a string of musical notes in a special ASCII format into a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes represented in a specific format, 
    returns a list of integers corresponding to the number of beats for each note.
    Format of input:
        'o o| .| .| ...'
    Each '.' is a whole note, lasting 4 beats, 
        'o' is a half note, lasting 2 beats, 
        'o|' is a whole note or half note, lasting 1 beat
    """
    beats: List[int] = []
    current_beat = 1

    for note in music_string:
        if note == '.' and current_beat == 1:
            current_beat = 0
        elif note == 'o':
            beats.append(current_beat)
            current_beat += 4
        elif note == 'o|':
            beats.append(current_beat)
            current_beat += 2
        elif note == '|':
            beats.append(current_beat)
            current_beat += 1
        else:
            print("Error, invalid note format")
            return []
    return beats
```
This function takes a music string in the format '.... o| ...'., and returns a list of integers representing the number of beats for each note.