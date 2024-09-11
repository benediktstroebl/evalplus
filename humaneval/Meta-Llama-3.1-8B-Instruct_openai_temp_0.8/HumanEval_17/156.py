```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map musical notes to their corresponding beat lengths
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beats = []

    # Iterate over each note in the string
    for note in notes:
        # Append the beat length of the current note to the list
        beats.append(note_to_beats[note])

    # Return the list of beat lengths
    return beats


# Test the function with example input
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format, parses the string, and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map musical notes to their corresponding beat lengths and then iterates over each note in the string to append its beat length to the list. The test case at the end demonstrates the function's usage with example input.