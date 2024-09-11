```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map each note to its corresponding duration in beats
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its duration to the list
            if current_note:
                durations.append(note_durations.get(current_note, 0))
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the duration of the last note to the list
    if current_note:
        durations.append(note_durations.get(current_note, 0))

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

You can also use a more concise version using regular expressions:

```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map each note to its corresponding duration in beats
    note_durations = {
        'o': 4,
        'o\|': 2,
        '\.\|': 1
    }

    # Find all notes in the input string using regular expressions
    notes = re.findall('|'.join(note_durations.keys()), music_string)

    # Return a list of durations corresponding to each note
    return [note_durations.get(note, 0) for note in notes]


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```