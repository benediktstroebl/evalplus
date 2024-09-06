```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parses a string representing musical notes in a special ASCII format into a list of integers.
    >>> music_string = 'o o| .| o| .| .| .| .| o o'
    notes = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    >>> parse_music('o o| .| o| .| .| .| .| .o')
    notes == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = []
    current_beat = 0
    for note in music_string.split(' '|' ):
        if note == 'o':
            notes.append(current_beat + 4)
            current_beat += 4
        elif note == 'o|':
            notes.append(current_beat + 2)
            current_beat += 2
        elif note == '.|':
            notes.append(current_beat)
            current_beat += 1
        else:
            raise ValueError("Invalid note")
    return notes
```