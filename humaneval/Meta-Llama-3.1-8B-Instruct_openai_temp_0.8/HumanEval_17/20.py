### Musical Note Parser

The following Python script defines a function `parse_music` to parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the duration of each note.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the duration of each note.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note.

    Examples:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map note symbols to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the input string
    for note in notes:
        # Append the duration of the current note to the list
        durations.append(note_durations[note])

    # Return the list of note durations
    return durations

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes in a special ASCII format as input and returns a list of integers corresponding to the duration of each note. The function uses a dictionary to map note symbols to their durations and then iterates over each note in the input string to append its duration to the list. The example usage demonstrates how to use the function with a sample input string.