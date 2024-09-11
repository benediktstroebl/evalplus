```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts.

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map each note to its beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to look up the beats for each note and return the list
    return [note_beats[note] for note in notes]


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this script, the `parse_music` function takes a string of musical notes, splits it into individual notes, and looks up the beats for each note in a dictionary. The list of beats is then returned. The example usage at the end demonstrates how to use the function with the provided input string.