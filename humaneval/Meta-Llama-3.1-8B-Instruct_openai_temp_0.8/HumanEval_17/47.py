```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map note characters to their corresponding beat values
    note_values = {
        'o': 4,   # whole note, lasts four beats
        'o|': 2,  # half note, lasts two beats
        '.|': 1   # quater note, lasts one beat
    }

    # Initialize an empty list to store the beat values
    beat_values = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the beat value of the current note to the list
        beat_values.append(note_values[note])

    # Return the list of beat values
    return beat_values

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses the string, and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map note characters to their corresponding beat values and splits the input string into individual notes before iterating over them and appending their beat values to a list. The script includes a test case at the end to demonstrate the function's usage.