### Music Note Parser
#### A Python Script to Parse Musical Notes from ASCII Format
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers
    corresponding to the number of beats each note lasts.

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    return [notes[note] for note in music_string.split()]


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes in ASCII format as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map each note to its corresponding beat duration.

You can add more notes to the dictionary as needed to support additional note types. The function uses list comprehension to parse the input string and extract the note durations.

The test case at the end demonstrates the function's usage and output.