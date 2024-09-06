Here's the Python code with a self-contained function that solves the problem of parsing and returning the number of beats for a given music string:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes represented in the format of ASCII characters as input and 
    returns a list of integers corresponding to the number of beats for each note.

    Here's legend:
    - 'o' represents whole notes, lasting four beats
    - 'o|' represents half notes, lasting two beats
    - '.|' represents quarter notes, lasting one beat

    Returns:
    A list of integers.
    """
    legend:
    music_notes = ['o o| .| o| .| .| .| .| .| o o']
    beats = [4, 2, 1, 2, 1, 1, 1, 1, 4]
    beats = [int(beat) for beat in music_notes]
    return beats
```