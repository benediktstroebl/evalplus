### Music Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the number of beats each note lasts.

    The input string is expected to be in a special ASCII format, where:
    - 'o' represents a whole note (4 beats)
    - 'o|' represents a half note (2 beats)
    - '.|' represents a quarter note (1 beat)

    Args:
        music_string (str): The input string of musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map note characters to their corresponding beat lengths
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note in the input string
    for note in notes:
        # Look up the beat length for the current note in the dictionary
        beat_lengths.append(note_beats[note])

    # Return the list of beat lengths
    return beat_lengths

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes as input, and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map note characters to their corresponding beat lengths, and then iterates over each note in the input string to build the list of beat lengths. The example usage at the end demonstrates how to call the function with a sample input string.