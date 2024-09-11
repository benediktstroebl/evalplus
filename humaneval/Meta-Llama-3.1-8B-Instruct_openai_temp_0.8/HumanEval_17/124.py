### Music Note Parser
#### Problem Description
Parse a string of musical notes in a special ASCII format and return a list of integers representing the number of beats each note lasts.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map note types to their corresponding beat lengths
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note and append its beat length to the list
    for note in notes:
        beat_lengths.append(note_lengths[note])

    # Return the list of beat lengths
    return beat_lengths

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script uses a dictionary to map note types to their corresponding beat lengths, then splits the input string into individual notes and iterates over them to append their beat lengths to a list. The function finally returns this list.