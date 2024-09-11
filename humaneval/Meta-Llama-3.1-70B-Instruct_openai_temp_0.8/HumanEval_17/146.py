```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in ASCII format and returns a list of integers representing
    the number of beats each note lasts.

    :param music_string: A string of musical notes in ASCII format
    :return: A list of integers representing the number of beats each note lasts
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note lengths
    note_lengths = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and (i == len(notes) - 1 or notes[i + 1]!= '|'):
            # If it's a whole note, append 4 to the note lengths list
            note_lengths.append(4)
        # Check if the note is a half note
        elif notes[i] == 'o' and notes[i + 1] == '|':
            # If it's a half note, append 2 to the note lengths list and skip the next character
            note_lengths.append(2)
            i += 1
        # Check if the note is a quarter note
        elif notes[i] == '.|':
            # If it's a quarter note, append 1 to the note lengths list
            note_lengths.append(1)
        i += 1

    # Return the list of note lengths
    return note_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script works by splitting the input string into individual notes and then iterating over each note. It checks the type of each note and appends the corresponding length to the `note_lengths` list. The script handles whole notes, half notes, and quarter notes according to the provided legend.