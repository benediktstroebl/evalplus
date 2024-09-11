```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over each note
    for note in notes:
        # Check the type of the note
        if note == 'o':
            # If the note is a whole note, add 4 to the list
            beat_lengths.append(4)
        elif note == 'o|':
            # If the note is a half note, add 2 to the list
            beat_lengths.append(2)
        elif note == '.|':
            # If the note is a quarter note, add 1 to the list
            beat_lengths.append(1)
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {note}")

    # Return the list of beat lengths
    return beat_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the number of beats each note lasts. The function splits the input string into individual notes, checks the type of each note, and adds the corresponding beat length to the list. The function then returns the list of beat lengths. The script also includes a test case to demonstrate the function's usage.