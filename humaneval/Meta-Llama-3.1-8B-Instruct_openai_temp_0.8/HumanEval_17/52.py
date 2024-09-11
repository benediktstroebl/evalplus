### Music Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers
    corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string of musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    return [note_dict[note] for note in music_string.split()]

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map each note to its corresponding beat value. The list comprehension then iterates over the input string, splitting it into individual notes and looking up their corresponding beat values in the dictionary. The result is a list of integers representing the number of beats each note lasts.