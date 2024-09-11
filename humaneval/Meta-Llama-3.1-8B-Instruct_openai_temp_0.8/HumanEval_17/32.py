```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    The notes are represented as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """

    # Split the input string by spaces to separate each note
    notes = music_string.split()

    # Initialize an empty list to store the length of each note
    note_lengths = []

    # Loop through each note in the list
    for note in notes:
        # Check the length of the note and append the corresponding length to the list
        if len(note) == 1:  # whole note
            note_lengths.append(4)
        elif len(note) == 2:  # half note
            note_lengths.append(2)
        elif len(note) == 3:  # quarter note
            note_lengths.append(1)

    # Return the list of note lengths
    return note_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the length of each note. The function loops through each note in the input string, checks its length, and appends the corresponding length to the output list. The script then tests the function with the provided example input.