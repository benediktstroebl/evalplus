```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Initialize an empty list to store the beats of each note
    beats = []

    # Loop through the music string
    i = 0
    while i < len(music_string):
        # Check if the current character is 'o' (whole note)
        if music_string[i] == 'o':
            # If it's a whole note, append its beats to the list
            beats.append(4)
            # Move to the next character
            i += 1

        # Check if the current character is 'o|' (half note)
        elif music_string[i:i+2] == 'o|':
            # If it's a half note, append its beats to the list
            beats.append(2)
            # Move to the next two characters
            i += 2

        # Check if the current character is '.|' (quater note)
        elif music_string[i:i+2] == '.|':
            # If it's a quater note, append its beats to the list
            beats.append(1)
            # Move to the next two characters
            i += 2

        # If the current character is not a note, raise a ValueError
        else:
            raise ValueError("Invalid note in music string")

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script will parse the input string and return the list of beats for each note as per the given legend. It handles whole notes, half notes, and quater notes, and raises a ValueError if it encounters an invalid note in the input string.