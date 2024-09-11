### Musical Note Parser
#### Problem Description
Parse a string representing musical notes in ASCII format and return a list of integers corresponding to the number of beats each note lasts.

#### Solution
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map each note to its corresponding beat duration
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    note_durations = []

    # Iterate over each note in the input string
    for note in notes:
        # Check if the note is in the dictionary
        if note in note_beats:
            # Append the note's duration to the list
            note_durations.append(note_beats[note])

    # Return the list of note durations
    return note_durations

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string representing musical notes in ASCII format as input, and returns a list of integers corresponding to the number of beats each note lasts. The function uses a dictionary to map each note to its corresponding beat duration, and then iterates over the input string to append the note durations to a list. The example usage at the end demonstrates how to use the function with a sample input string.