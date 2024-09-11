### Music Note Parser

#### Problem Description
Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to the number of beats each note lasts.

#### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    Examples:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map note symbols to their corresponding beat values
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to look up the beat value for each note and append it to the result list
    return [note_to_beats[note] for note in notes]

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Explanation
The provided code defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map note symbols to their corresponding beat values, then splits the input string into individual notes and uses a list comprehension to look up the beat value for each note and append it to the result list. The example usage demonstrates how to call the function with a sample input string.