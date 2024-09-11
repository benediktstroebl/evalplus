```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    Args:
        music_string (str): A string of musical notes

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts
    """
    # Define a dictionary to map musical notes to their corresponding beat lengths
    note_beat_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the list
    for note in notes:
        # Append the beat length of the current note to the list
        beat_lengths.append(note_beat_lengths[note])

    # Return the list of beat lengths
    return beat_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map musical notes to their corresponding beat lengths, and then iterates over the input string to append the beat lengths to a list. The test at the end demonstrates the function's usage and expected outcome.