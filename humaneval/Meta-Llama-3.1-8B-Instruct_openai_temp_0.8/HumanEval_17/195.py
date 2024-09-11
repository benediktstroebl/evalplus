```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes in the specified format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map notes to their corresponding beat values
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat values
    beat_values = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the list
    for note in notes:
        # Append the beat value of the current note to the list
        beat_values.append(note_values.get(note, 0))

    # Return the list of beat values
    return beat_values

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in a special ASCII format and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map notes to their corresponding beat values and then iterates over each note in the input string, appending its beat value to the list. The script also includes a test case to demonstrate the function's usage.