```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Define a dictionary to map note types to their corresponding beat values
    note_map = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into notes and process them one by one
    notes = music_string.split()
    beat_values = []

    for note in notes:
        # Check if the note is valid (i.e., it exists in the note dictionary)
        if note in note_map:
            # Append the beat value of the note to the list
            beat_values.append(note_map[note])
        else:
            # If the note is invalid, raise a ValueError
            raise ValueError(f"Invalid note: {note}")

    return beat_values

# Test the function with the provided example
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map note types to their corresponding beat values and splits the input string into individual notes to process them one by one. If an invalid note is encountered, it raises a `ValueError`.