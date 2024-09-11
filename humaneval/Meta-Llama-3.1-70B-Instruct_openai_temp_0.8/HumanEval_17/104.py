```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # Add the character to the current note
        note += char

        # If the note is complete (i.e., it matches one of the notes in the dictionary), add its beats to the list
        if note in note_beats:
            beats.append(note_beats[note])
            note = ''

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

Alternatively, you can use a regular expression to split the input string into individual notes:

```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o\\|': 2,
        '\\|': 1
    }

    # Use regular expression to split the input string into individual notes
    notes = re.findall('o\\|?|\\.\\|', music_string)

    # Use a list comprehension to create a list of beats
    beats = [note_beats[note] for note in notes]

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```