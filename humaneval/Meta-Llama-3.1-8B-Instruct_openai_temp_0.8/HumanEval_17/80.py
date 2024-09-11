```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in ASCII format and returns a list of integers representing how many beats each note lasts.

    :param music_string: A string representing musical notes in ASCII format
    :return: A list of integers representing how many beats each note lasts
    """

    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats
    beats = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the beats for the current note to the list
        beats.append(note_beats.get(note, 0))  # Get returns None if note is not found, we use 0 as default value

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in ASCII format and returns a list of integers representing how many beats each note lasts. The function uses a dictionary to map notes to their corresponding beats and then splits the input string into individual notes, iterating over each note to append its beats to the list. The function also includes a test case to demonstrate its usage.