Here's a self-contained Python function that solves the problem of parsing musical notes into a list of integers representing the number of beats each note lasts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

    Here is legend:
    - 'o' represents whole notes, lasting four beats
    - 'o|' represents half notes, lasting two beats
    - '.|' represents quarter notes, lasting one beat

    >>>[int32] music_string: ['o o| .| o| .| .| .| .| o o']
    >>> parse_music(music_string)
    [4, 2, 1, 2, 1, 1, 1, 1, 4]
    """
    return [len(x) for x in music_string.split(" "|")]
```
This function uses list comprehension to split the input string by the ASCII character '|', which represents the split between a quarter note and a rest. After splitting, it converts each quarter note and rest into an integer using the len() function. The resulting list contains the core parts of the input string, and the length of each represents how many beats a particular note lasts.