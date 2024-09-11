```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string of musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.

    """
    # Define a dictionary to map notes to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the list
    for note in notes:
        # Append the duration of the current note to the list of durations
        durations.append(note_durations[note])

    # Return the list of note durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in ASCII format as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map notes to their corresponding durations, and then splits the input string into a list of notes. It then iterates over each note in the list and appends its duration to a list of durations, which is finally returned by the function. The script also includes a test case to demonstrate the function's behavior.