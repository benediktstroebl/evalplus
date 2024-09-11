### Music Note Parser Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.

    Args:
    music_string (str): A string containing musical notes in the format 'o' (whole note), 'o|' (half note), '.|' (quarter note).

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """

    # Create a dictionary mapping note formats to their corresponding beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to look up the duration of each note and add it to the result list
    result = [note_durations[note] for note in notes]

    return result

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map note formats to their corresponding durations, and a list comprehension to efficiently create the output list. The example usage at the end demonstrates how to use the function to parse a string of musical notes.