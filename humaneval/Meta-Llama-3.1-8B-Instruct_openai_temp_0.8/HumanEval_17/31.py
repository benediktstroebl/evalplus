### Musical Note Parser
#### Solution in Python
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a musical note string and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    Examples:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    return [note_dict[note] for note in music_string.split()]

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the number of beats each note lasts. The function uses a dictionary to map the note characters to their respective beat values, and a list comprehension to split the input string into individual notes and extract their beat values.