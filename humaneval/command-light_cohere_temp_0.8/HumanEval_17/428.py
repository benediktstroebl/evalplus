```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes, represented in a special format, 
    and parses it to return a list of integers corresponding to how many beats does each note last. 

    legend: 
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: str - input to function
    :return: List[int] - List of integers, where each integer represents the number of beats until the next note
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.pyth input 
    ' music_string='"o o| .| o| .| .| .| .| o o"']
```