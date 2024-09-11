```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers 
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes in the format 'o', 'o|', '.|', etc.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.

    Examples:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    durations = []

    # Iterate over each note
    for note in notes:
        # If the note is 'o', it lasts 4 beats
        if note == 'o':
            durations.append(4)
        # If the note is 'o|', it lasts 2 beats
        elif note == 'o|':
            durations.append(2)
        # If the note is '.|', it lasts 1 beat
        elif note == '.|':
            durations.append(1)

    # Return the list of note durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in the specified format and returns a list of integers representing the number of beats each note lasts. The function uses if-elif statements to determine the duration of each note based on its ASCII representation. The script then tests the function with the provided example input.