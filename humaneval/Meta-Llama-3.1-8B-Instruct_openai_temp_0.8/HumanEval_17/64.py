### Music Parser Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    parsed_music = []
    for note in music_string.split():
        if note in note_lengths:
            parsed_music.append(note_lengths[note])
        else:
            raise ValueError(f"Unknown note: {note}")

    return parsed_music


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script uses a dictionary to map the musical notes to their respective lengths. It then splits the input string into individual notes, looks up each note in the dictionary, and appends its length to the result list. If an unknown note is encountered, it raises a ValueError.