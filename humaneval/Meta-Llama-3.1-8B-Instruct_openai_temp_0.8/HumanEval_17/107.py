### Music Note Parser
#### Problem Description

This script parses a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map note strings to their beat values
    note_dict = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into a list of notes
    notes = music_string.split()

    # Use a list comprehension to create a list of beat values
    beat_values = [note_dict[note] for note in notes]

    return beat_values

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Explanation

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the beats each note lasts. The function uses a dictionary `note_dict` to map note strings to their beat values, and then uses a list comprehension to create the output list.