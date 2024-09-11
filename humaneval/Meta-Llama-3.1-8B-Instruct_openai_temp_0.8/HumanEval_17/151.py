```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string of musical notes in the specified ASCII format.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Dictionary to map note types to their corresponding beat durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the result
    result = []

    # Iterate over each note
    for note in notes:
        # Append the duration of the current note to the result list
        result.append(note_durations[note])

    # Return the result list
    return result

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script uses a dictionary to map note types to their corresponding beat durations, then splits the input string into individual notes and appends their durations to a result list. The result list is then returned by the function.