### Parse Music Notes
#### Problem Description

The following Python script takes a string representing musical notes in a special ASCII format, parses the string, and returns a list of integers corresponding to how many beats each note lasts.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Define a dictionary to map note types to their corresponding beat lengths
    note_types = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to parse each note and calculate its beat length
    beat_lengths = [note_types[note] for note in notes]

    return beat_lengths

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

#### Explanation

This script defines a function `parse_music` that takes a string `music_string` as input and returns a list of integers corresponding to how many beats each note lasts.

Inside the function, a dictionary `note_types` is defined to map note types to their corresponding beat lengths. The input string is then split into individual notes using the `split` method.

A list comprehension is used to parse each note and calculate its beat length. The `note_types` dictionary is used to look up the beat length for each note, and the result is appended to the `beat_lengths` list.

Finally, the function returns the `beat_lengths` list. In the example usage, the `parse_music` function is called with a sample input string, and the resulting list of beat lengths is printed to the console.