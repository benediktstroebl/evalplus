### Musical Note Parser
#### Problem Statement
Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the number of beats each note lasts.

#### Solution
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Define a dictionary to map note representations to their corresponding beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '|': 1
    }

    # Initialize an empty list to store the parsed note durations
    parsed_notes = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Append the duration of the current note to the parsed notes list
        parsed_notes.append(note_durations.get(note, 0))

    # Return the list of parsed note durations
    return parsed_notes

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script uses a dictionary to map note representations to their corresponding beat durations. It then splits the input string into individual notes, iterates over each note, and appends its duration to a list. Finally, it returns the list of parsed note durations.