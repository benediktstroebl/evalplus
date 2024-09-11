```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Define a dictionary to map each note to its corresponding beat duration
    note_duration = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into a list of notes
    notes = music_string.split()

    # Use a list comprehension to convert each note to its corresponding beat duration
    beat_durations = [note_duration[note] for note in notes]

    return beat_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes as input, 
and returns a list of integers corresponding to how many beats each note lasts. The function uses a 
dictionary to map each note to its corresponding beat duration, and then uses a list comprehension 
to convert each note to its corresponding beat duration. The script includes a test case to verify 
that the function works correctly.