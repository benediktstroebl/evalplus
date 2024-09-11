### Music Note Parser
#### A Python Script to Parse Musical Notes from ASCII Strings
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the duration of each note.

    Args:
    music_string (str): A string of musical notes, where 'o' is a whole note (4 beats), 'o|' is a half note (2 beats), and '.|' is a quarter note (1 beat).

    Returns:
    List[int]: A list of integers representing the duration of each note in the input string.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map note characters to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the note durations
    note_duration_list = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Append the duration of the current note to the note_duration_list
        note_duration_list.append(note_durations[note])

    # Return the list of note durations
    return note_duration_list

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```
This script defines a function `parse_music` that takes a string of musical notes in ASCII format as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map note characters to their corresponding durations and splits the input string into individual notes to extract their durations. The example usage at the end demonstrates how to call the function with a sample input string and print the resulting list of note durations.