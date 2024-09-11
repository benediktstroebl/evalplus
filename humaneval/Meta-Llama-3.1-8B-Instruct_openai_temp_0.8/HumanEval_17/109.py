```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to the number of beats each note lasts.

    The legend for the notes is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): The string of musical notes to parse.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    note_durations = []

    # Define a dictionary to map each note to its duration
    note_duration_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Iterate over each note in the input string
    for note in notes:
        # Append the duration of the current note to the list
        note_durations.append(note_duration_map[note])

    # Return the list of note durations
    return note_durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map each note to its duration and iterates over the input string to build the list of note durations. The example usage at the end demonstrates how to call the function with a sample input string.