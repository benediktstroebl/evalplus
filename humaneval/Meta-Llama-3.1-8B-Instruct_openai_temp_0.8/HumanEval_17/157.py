```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    The legend for the musical notes is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map musical notes to their corresponding beats
    note_map = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to convert each note to its corresponding beats
    beats = [note_map[note] for note in notes]

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses it, and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map each musical note to its corresponding beats, and then uses a list comprehension to convert each note to its corresponding beats. The script also includes a test case to demonstrate the function's usage.