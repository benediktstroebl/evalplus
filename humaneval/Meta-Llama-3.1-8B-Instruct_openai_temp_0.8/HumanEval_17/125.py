```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function parses a given musical note string and returns a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map musical notes to their corresponding beat lengths
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Initialize an index to keep track of the current position in the music string
    i = 0

    # Loop through the music string
    while i < len(music_string):
        # If the current character is a note, append its beat length to the list
        if music_string[i] in note_lengths:
            beat_lengths.append(note_lengths[music_string[i:i+2]])
            # Move the index forward by 2 characters (since we're using a substring)
            i += 2
        else:
            # If the current character is not a note, raise a ValueError
            raise ValueError("Invalid musical note: " + music_string[i])

    # Return the list of beat lengths
    return beat_lengths


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to the number of beats each note lasts. It uses a dictionary to map musical notes to their corresponding beat lengths and loops through the music string to build the list of beat lengths. The script also includes a test case to demonstrate the function's usage.