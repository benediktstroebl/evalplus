```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Define a dictionary to map note types to their corresponding beat durations
    note_types = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Iterate over each note in the input string
    for note in notes:
        # Append the beat duration of the current note to the list
        beat_durations.append(note_types[note])

    # Return the list of beat durations
    return beat_durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes as input and returns a list of integers corresponding to how many beats each note lasts. The function first splits the input string into individual notes, then iterates over each note, appending its corresponding beat duration to a list. Finally, the list of beat durations is returned. The example usage at the end demonstrates how to use the function to parse a string of musical notes.