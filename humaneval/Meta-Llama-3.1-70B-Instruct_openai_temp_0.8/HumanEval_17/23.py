```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the number of beats for each note.
    """

    # Create a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over the notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i < len(notes) - 1 and notes[i + 1] == 'o':
            # If it is, add the beats for a whole note to the list and increment the index by 2
            beats.append(note_beats['o'])
            i += 2
        # Check if the current note is a half note or quarter note
        elif notes[i] in ['o|', '.|']:
            # If it is, add the beats for the note to the list and increment the index by 1
            beats.append(note_beats[notes[i]])
            i += 1
        else:
            # If it is a standalone whole note
            beats.append(note_beats['o'])
            i += 1

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script works by iterating over the input string and splitting it into individual notes. It then checks each note to see if it matches one of the known note symbols and adds the corresponding number of beats to the list. The function handles standalone whole notes, half notes, and quarter notes correctly.