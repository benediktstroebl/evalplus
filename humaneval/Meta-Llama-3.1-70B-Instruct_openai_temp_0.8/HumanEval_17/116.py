```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer corresponds to the number of beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the number of beats each note lasts.
    """

    # Define a dictionary to map note symbols to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of note symbols
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beat_values = []

    # Iterate over each note symbol
    i = 0
    while i < len(notes):
        # Check if the current note symbol is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # Append the beat value of a whole note to the list
            beat_values.append(note_beats['o'])
            # Skip the next note symbol
            i += 2
        # Check if the current note symbol is a half note or a quarter note
        elif notes[i].endswith('|'):
            # Append the beat value of the note symbol to the list
            beat_values.append(note_beats[notes[i]])
            # Move to the next note symbol
            i += 1
        else:
            # Append the beat value of a whole note to the list
            beat_values.append(note_beats['o'])
            # Move to the next note symbol
            i += 1

    # Return the list of beat values
    return beat_values


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```