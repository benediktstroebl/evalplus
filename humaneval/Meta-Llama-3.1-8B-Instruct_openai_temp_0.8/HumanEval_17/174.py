```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers
    corresponding to the beats each note lasts.

    Args:
    music_string (str): A string of musical notes.

    Returns:
    List[int]: A list of integers representing the beats each note lasts.

    Notes:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """

    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string by spaces to get a list of notes
    notes = music_string.split()

    # Use a list comprehension to replace each note with its corresponding value
    beats = [note_values[note] for note in notes]

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

In this script, we first define a dictionary `note_values` that maps each note to its corresponding beat value. We then split the input string by spaces to get a list of notes. Using a list comprehension, we replace each note with its corresponding value from the dictionary. The resulting list of beat values is then returned by the function.