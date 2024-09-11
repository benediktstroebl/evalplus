```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in ASCII format and returns a list of integers
    corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string of musical notes in ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map notes to their beat values
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beat_values = []

    # Iterate over each note
    for note in notes:
        # Append the beat value of the current note to the list
        beat_values.append(note_beats[note])

    # Return the list of beat values
    return beat_values


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers corresponding to the number of beats each note lasts. It uses a dictionary to map notes to their beat values and then splits the input string into individual notes.