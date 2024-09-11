```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to the number of beats each note lasts.

    The legend is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Create a dictionary to map note types to their corresponding beat values
    note_dict = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat values
    beat_values = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Append the beat value of the current note to the list
        beat_values.append(note_dict[note])

    # Return the list of beat values
    return beat_values


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the number of beats each note lasts. The function uses a dictionary to map note types to their corresponding beat values and then iterates over each note in the input string to append the beat value to the list. The script includes a test case to demonstrate the function's usage.