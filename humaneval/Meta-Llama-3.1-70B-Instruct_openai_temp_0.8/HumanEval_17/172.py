```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """
    # Define a dictionary to map note representations to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over the list of notes
    for note in notes:
        # If the current note is not empty and the current character is a space,
        # it means we've reached the end of a note, so add its duration to the list
        if current_note and note == '':
            durations.append(note_durations[current_note])
            current_note = ''
        # If the current note is empty, add the current character to it
        elif not current_note:
            current_note = note
        # If the current note is not empty and the current character is not a space,
        # add the current character to the current note
        else:
            current_note +='' + note

        # If the current note is a complete note (i.e., it's in the note_durations dictionary),
        # add its duration to the list and reset the current note
        if current_note in note_durations:
            durations.append(note_durations[current_note])
            current_note = ''

    # Return the list of note durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
However, the given code may not work correctly if the input string contains multiple spaces between the notes or if the notes are not separated by spaces at all. 

Here is a more robust version of the function that uses regular expressions to split the input string into notes:

```python
from typing import List
import re

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """
    # Define a dictionary to map note representations to their corresponding durations
    note_durations = {
        'o': 4,
        'o\\|': 2,
        '\\|': 1
    }

    # Use regular expressions to split the input string into a list of notes
    notes = re.findall('|'.join(note_durations.keys()), music_string)

    # Use a list comprehension to get the duration of each note
    durations = [note_durations[note] for note in notes]

    # Return the list of note durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This version of the function should work correctly even if the input string contains multiple spaces between the notes or if the notes are not separated by spaces at all.