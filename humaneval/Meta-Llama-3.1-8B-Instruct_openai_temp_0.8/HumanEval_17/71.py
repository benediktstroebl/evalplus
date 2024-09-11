```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Examples:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Initialize an empty list to store the duration of each note
    note_durations = []

    # Loop through the input string two characters at a time (except for the last character)
    for i in range(0, len(music_string), 2):
        # Check if the current character and the next one form a complete note
        if i + 1 < len(music_string):
            # Check the note type and append its duration to the list
            if music_string[i:i+2] == 'o|':
                note_durations.append(2)
            elif music_string[i:i+2] == '.|':
                note_durations.append(1)
            elif music_string[i] == 'o':
                note_durations.append(4)
            elif music_string[i] == '.':
                note_durations.append(1)

    # Return the list of note durations
    return note_durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses it, and returns a list of integers representing the duration of each note. The function uses a loop to iterate through the input string two characters at a time, checks each pair of characters to determine the note type, and appends the corresponding duration to the list. Finally, the function returns the list of note durations. The example usage at the end demonstrates how to call the function with a sample input string.