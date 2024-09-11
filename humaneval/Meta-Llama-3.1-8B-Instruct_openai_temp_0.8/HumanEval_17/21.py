```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.

    Examples:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beat_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to look up the beat duration for each note and return the result
    return [beat_durations[note] for note in notes]


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes in a special ASCII format and returns a list of integers corresponding to the number of beats each note lasts. The function uses a dictionary to map each note type to its corresponding beat duration. It then splits the input string into individual notes, looks up the beat duration for each note, and returns the result. The script also includes a test case to demonstrate the function's behavior.