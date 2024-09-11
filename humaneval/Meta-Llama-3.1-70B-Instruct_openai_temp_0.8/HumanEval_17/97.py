```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string, and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note lengths
    note_lengths = []

    # Iterate over each note in the notes list
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1]!= '|':
            # Append the whole note length (4) to the note_lengths list
            note_lengths.append(4)
        # Check if the note is a half note
        elif notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # Append the half note length (2) to the note_lengths list
            note_lengths.append(2)
            # Skip the '|' character
            i += 1
        # Check if the note is a quarter note
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            # Append the quarter note length (1) to the note_lengths list
            note_lengths.append(1)
            # Skip the '|' character
            i += 1
        i += 1

    # Return the list of note lengths
    return note_lengths


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```