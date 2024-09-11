### Music Note Parser

This script defines a function `parse_music` to parse a string of musical notes represented in a special ASCII format and returns a list of integers representing the number of beats each note lasts.

#### Code
```markdown
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Define a dictionary to map note types to their corresponding beat values
    note_map = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string by spaces to get a list of notes
    notes = music_string.split()

    # Use a list comprehension to convert each note to its corresponding beat value
    beats = [note_map[note] for note in notes]

    return beats

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes as input, splits the string into individual notes, and uses a dictionary to map each note type to its corresponding beat value. The function then returns a list of integers representing the number of beats each note lasts. The example usage demonstrates how to use the function to parse a string of musical notes and print the resulting list of beat values.