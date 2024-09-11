### Music Note Parser
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parses a string of musical notes and returns a list of integers representing the duration of each note.

    The input string uses the following notation:
    - 'o' represents a whole note (4 beats)
    - 'o|' represents a half note (2 beats)
    - '.|' represents a quarter note (1 beat)

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note.
    """
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    return [note_dict[note] for note in notes]


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, splits the string into individual notes, and uses a dictionary to map each note to its corresponding duration. The function returns a list of integers representing the duration of each note. The example usage at the end demonstrates how to use the function to parse a string of musical notes.