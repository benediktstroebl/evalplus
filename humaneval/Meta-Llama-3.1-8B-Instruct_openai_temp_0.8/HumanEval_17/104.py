```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the duration of each note.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note.
    """

    # Define a dictionary to map musical notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Iterate over each note in the list of notes
    for note in notes:
        # Get the duration of the current note from the dictionary
        duration = note_durations[note]
        
        # Append the duration to the list of durations
        durations.append(duration)

    # Return the list of durations
    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses the string, and returns a list of integers corresponding to the duration of each note. The function uses a dictionary to map musical notes to their durations, and it iterates over the input string to get the duration of each note. The script also includes an example usage to demonstrate how to call the function.