```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and returns a list of integers corresponding to the beats of each note.

    Notes are formatted as 'o' whole note (lasts four beats),
    'o|' half note (lasts two beats),
    '.|' quarter note (lasts one beat).

    >>> parse_music('o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

    """

    notes = []
    is_half_note = lambda c: c == 'o|'
    is_quarter_note = lambda c: c == '.|'
    for note in music_string.replace():
        if is_half_note(note):
        notes.append(2)
    elif is_quarter_note(note):
        notes.append(1)
    else:
        notes.append(4)

    return notes
```