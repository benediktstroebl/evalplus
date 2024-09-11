```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the duration of each note.

    Args:
        music_string (str): A string of musical notes in the format 'o', 'o|', or '.|'.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map note types to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the note durations
    durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Get the duration of the current note from the dictionary
        duration = note_durations.get(note, 0)

        # Append the duration to the list
        durations.append(duration)

    # Return the list of note durations
    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map note types to their durations, then splits the input string into individual notes and appends their durations to a list. The function finally returns this list of note durations. The example usage at the end demonstrates how to use the function to parse a string of musical notes and print the resulting list of note durations.