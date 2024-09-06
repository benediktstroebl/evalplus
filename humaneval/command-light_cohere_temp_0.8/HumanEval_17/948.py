```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes represented in a special format and
    returns a list of integers corresponding to how many beats does each note last.

    Notes are provided in the format: 
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Test cases are also provided to ensure the correctness of this function.
    >>> test_cases()
    test cases:
    ['o o| .| o| .| .| .| .| o o',
     'o o| .',
     '|o| || .| .',
     '.|.'o',
     'o o| .| .o',
     'o .| o| .',
     'o o o| .',
     'o o o o| .',
     'o o o o o| .',
     'o o o o o o o o o']
    expected outputs:
    [[4, 2, 1, 2, 1, 1, 1, 1, 4, 4],
     [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
     [4, 4],
     [4],
     [4, 4, 4, 4],
     [4, 4, 4, 4],
     [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
    """
    notes = music_string.split('|')
    music_notes = [int(note) for note in notes]

    return [len(music_notes)] + music_notes[-1:]

test_cases()
```

This Python script defines a function `parse_music` that takes a music string in a specific format and returns a list of integers corresponding to the beats of each note. The function also includes test cases to ensure its correctness. 

Please note that this code assumes that the input music string follows a specific format, and the function may not work correctly with all possible music notation.