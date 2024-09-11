```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    The legend is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
    music_string (str): A string of musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Loop over each note
    for note in notes:
        # Check the type of note
        if note == 'o':  # whole note
            beats.append(4)
        elif note == 'o|':  # half note
            beats.append(2)
        elif note == '.|':  # quater note
            beats.append(1)
        else:
            # If the note is not recognized, skip it
            continue

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to how many beats each note lasts. The function uses a simple loop to iterate over each note in the input string, checks the type of note using if-elif-else statements, and appends the corresponding number of beats to the `beats` list. Finally, the script tests the function with the example input provided.