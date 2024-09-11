```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return a list of integers corresponding to the duration of each note.

    Args:
    music_string (str): A string representing musical notes. 'o' represents a whole note (4 beats), 'o|' represents a half note (2 beats), and '.|' represents a quarter note (1 beat).

    Returns:
    List[int]: A list of integers representing the duration of each note in the input string.
    """

    # Define a dictionary to map note characters to their corresponding durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the note durations
    note_durations_list = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Append the duration of the current note to the list
        note_durations_list.append(note_durations[note])

    # Return the list of note durations
    return note_durations_list

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in ASCII format as input, and returns a list of integers representing the duration of each note. The function uses a dictionary to map note characters to their corresponding durations, and then splits the input string into individual notes before iterating over each note to append its duration to the list. The script includes an example usage at the end to demonstrate how to use the function.