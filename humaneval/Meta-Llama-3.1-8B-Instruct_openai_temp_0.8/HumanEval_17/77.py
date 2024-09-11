Here's a Python function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers
    corresponding to the duration of each note in beats.

    The following legend is used:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note in beats.
    """
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to create a list of note durations
    return [note_durations[note] for note in notes]

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This function defines a dictionary `note_durations` that maps each note to its corresponding duration. It then splits the input string into individual notes using the `split()` method. Finally, it uses a list comprehension to create a list of note durations.