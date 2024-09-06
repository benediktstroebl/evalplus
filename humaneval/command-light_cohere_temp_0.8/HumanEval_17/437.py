Here's a self-contained Python script that defines a function `parse_music` to parse a string representing musical notes and returns a list of integers corresponding to the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes in a special ASCII format. 
   
    Task is to parse this string and return a list of integers, 
    corresponding to how many beats each note lasts.

    Notes:
    'o' whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Test cases:
    >>> parse_music('o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    """
    # First, separate all the notes
    notes = music_string.split('o chain|')
    beats = []
    for note in notes:
        # Remove the 'o|' or '.|' from the end of the string
        while note.endswith('|'):
            note = note[:-len(note)-2]
        # If the note is empty, it's a rest, so we add a single beat
        if note == '':
            beats.append(1)
        # Otherwise, it's a note, so we add four beats
        beats.append(4)
    return beats
```