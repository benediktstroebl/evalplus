```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers 
    corresponding to the duration of each note in beats.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map note types to their corresponding durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the parsed note durations
    parsed_notes = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the string
    for note in notes:
        # Append the duration of the current note to the parsed_notes list
        parsed_notes.append(note_durations[note])

    # Return the list of parsed note durations
    return parsed_notes


# Test the function with the provided example
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note in beats. The function uses a dictionary to map note types to their corresponding durations and then iterates over the input string to parse the note durations. The test case at the end demonstrates the function's behavior with the provided example input.