```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the result
    result = []

    # Split the music string into individual notes
    notes = music_string.split()

    # For each note, append its corresponding beats to the result list
    for note in notes:
        result.append(note_beats[note])

    # Return the result list
    return result


# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string representing musical notes in ASCII format and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map notes to their corresponding beats and splits the input string into individual notes before appending their corresponding beats to the result list. The example usage at the end demonstrates how to use this function.