```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Inputs a string representing musical notes in a special ASCII format and returns a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    parsed_notes = music_string.split()
    return [note_lengths[note] for note in parsed_notes]

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script uses a dictionary to map each note to its corresponding length, then splits the input string into individual notes and uses a list comprehension to create a list of their lengths.