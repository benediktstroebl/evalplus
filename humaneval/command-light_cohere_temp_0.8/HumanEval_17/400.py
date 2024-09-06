Here is a Python script that defines a function `parse_music` which takes a string music_string as input and returns a list of integers that correspond to the number of beats in the input music:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string in a special format representing musical notes and returns a list of integers corresponding to the number of beats each note lasts.

    The legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Returns:
    A list of integers corresponding to the number of beats each note lasts.
    """
    legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    # Use regular expressions to split the string by spaces and split by notes
    notes = music_string.split('o fact_')

    # Use a dictionary to map the notes to the number of beats
    beats = {'o': 4, 'o|': 2, '|': 1}

    # Create the output list
    output = []
    for note in notes:
        output.append(beats[note])

    return output
```

This script provides a simple solution for the given problem. The `parse_music` function uses regular expressions to split the input string by spaces and then splits by notes to map the notes to the number of beats. The function then creates a output list by appending the number of beats corresponding to each note.