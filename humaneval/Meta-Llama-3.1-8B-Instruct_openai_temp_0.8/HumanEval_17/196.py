### Music Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.split()
    return [note_map[note] for note in notes]

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, splits it into individual notes, and uses a dictionary to map each note to its corresponding number of beats. The function returns a list of integers representing the number of beats each note lasts.

The example usage at the end demonstrates how to use the `parse_music` function to parse a string of musical notes and print the resulting list of beat durations.