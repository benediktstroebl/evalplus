Here is a Python script that contains a self-contained function that solves the problem of parsing musical notes in a string and returns a list of integers representing the number of beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes represented in a specific format,
    and parses the string into a list of integers corresponding to the number of beats.
    Each note has a following format: 
    'o' - whole note, lasting 4 beats
    'o|' - half note, lasting 2 beats
    '.|' - quarter note, lasting 1 beat.
    The input string is parsed into a list of integers in the format [number_of_beats...].
    """
    # Define a mapping of musical notes to beats
    musical_notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Parse the input string into a list of integers
    notes = [musical_notes[note] for note in music_string.

    return notes

```
This function is self-contained and can be used to parse any input string of musical notes into the desired format.