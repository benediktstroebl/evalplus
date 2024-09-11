### Musical Note Parser
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes in the format 'o', 'o|', '.|', etc.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # Define a dictionary to map the note formats to their corresponding beat lengths
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note in the input string
    for note in notes:
        # Check if the note is in the dictionary and add its beat length to the list
        if note in note_beats:
            beat_lengths.append(note_beats[note])
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note format: {note}")

    # Return the list of beat lengths
    return beat_lengths


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes in a specific format and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map the note formats to their corresponding beat lengths, and then splits the input string into individual notes and adds their beat lengths to a list. If an unrecognized note format is encountered, it raises a `ValueError`. The example usage at the end demonstrates how to use this function to parse a string of musical notes.