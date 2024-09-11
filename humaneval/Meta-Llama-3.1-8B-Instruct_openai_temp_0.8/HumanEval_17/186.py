```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats
    beats = []

    # Iterate over each character in the music string
    for note in music_string.split():
        # If the note is in the dictionary, append its beats to the list
        if note in note_beats:
            beats.append(note_beats[note])
        # If the note is not in the dictionary, raise a ValueError
        else:
            raise ValueError(f"Invalid note: {note}")

    # Return the list of beats
    return beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map musical notes to their corresponding beats and iterates over each character in the input string to parse the notes. If an invalid note is encountered, a `ValueError` is raised. The script also includes an example usage of the function.