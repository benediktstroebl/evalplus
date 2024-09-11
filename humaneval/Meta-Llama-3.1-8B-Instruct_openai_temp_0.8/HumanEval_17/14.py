```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    The format is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map note types to their corresponding beat lengths
    note_types = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Split the music string into individual notes
    notes = music_string.split()

    # Iterate over each note in the music string
    for note in notes:
        # Append the beat length of the current note to the list
        beat_lengths.append(note_types.get(note, 0))

    # Return the list of beat lengths
    return beat_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes as input and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map note types to their corresponding beat lengths, and iterates over each note in the input string to build the list of beat lengths. The function is then tested with a sample input string.