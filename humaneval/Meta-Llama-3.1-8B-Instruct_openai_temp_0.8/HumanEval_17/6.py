```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    The notes are encoded as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string of musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Initialize an empty list to store the beat lengths
    beats = []

    # Split the music string into individual notes
    notes = music_string.split()

    # Iterate over each note in the music string
    for note in notes:
        # Check the type of note and append the corresponding beat length to the list
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)

    # Return the list of beat lengths
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in the special ASCII format and returns a list of integers corresponding to how many beats each note lasts. It uses a dictionary to map the note types to their corresponding beat lengths, and then splits the input string into individual notes and iterates over them to append the corresponding beat lengths to the list. The function is then tested with a sample input string.