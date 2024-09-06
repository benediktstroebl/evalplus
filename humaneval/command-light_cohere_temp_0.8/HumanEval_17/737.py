```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a music string in the format of different notes.

    Here is legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Return list of integers, each corresponding to how many beats each note lasts.
    """

    test cases:
    >>> parse_music('o o| .| o| .| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    >>> parse_music('o o| .o| .| .| .')
    [1, 2, 1, 1]
    >>> parse_music('.|o| .o| .| .| .')
    [1, 2, 1]
    """
    notes = music_string.split('|')
   
    whole_notes = [int(note) for note in notes if note.strip('o everyone of . test cases).

    beats = []
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
        else:
            beats.append(int(note))

    return beats
```