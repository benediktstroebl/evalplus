```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to the duration of each note in beats.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note in beats.

    Legend:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat
    """
    # Define a dictionary to map note formats to their durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into notes
    notes = music_string.split()

    # Use a list comprehension to get the duration of each note and return the result
    return [note_durations[note] for note in notes]


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers representing the duration of each note. The function uses a dictionary `note_durations` to map note formats to their durations, and then uses a list comprehension to get the duration of each note. The script includes a test case to demonstrate the function's behavior.