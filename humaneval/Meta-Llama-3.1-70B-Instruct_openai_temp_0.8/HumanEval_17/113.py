```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map note representations to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values of the notes
    beat_values = []

    # Iterate over the notes
    for note in notes:
        # Check if the note is in the dictionary
        if note in note_beats:
            # If it is, append its beat value to the list
            beat_values.append(note_beats[note])
        elif note == 'o':
            # Special case for whole notes without the '|' symbol
            beat_values.append(4)

    # Return the list of beat values
    return beat_values

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```