Here's the code to solve your markdown code parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string in the format of a musical score, represented
    with special ASCII characters. It should be a A list of integers,
    where each integer corresponds to how many beats does each note last.
    Here's legend:
        'o' - whole note, lasts 4 beats (must be a 4)
        'o/' - half note, lasts 2 beats (must be a 2)
        '.' - quarter note, lasts 1 beat

    >>> help parse_music('o o/o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    """
    notes = music_string.split("o <
    to beat'

    notes = [beat for beat in notes if beat.startswith('o o')] + [beat for beat in notes if beat.startswith('o '|')]
    notes = [int(note) for note in notes for note in ' '.join if note.isalpha()]
    struct: Begins with a whole note, then moves to a half note and so on.
    }


return notes
``` 
The function splits the string by each character that is not a '.' or beat and then converts each string to an integer and adds it to a list.  Finally, it checks if the list contains only whole notes (begins with 'o' and ends with 'o'), half notes (begins with 'o/'), and quarter notes ('|').  The function then returns the list of integers.