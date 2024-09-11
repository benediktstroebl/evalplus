```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format,
    parses the string, and returns a list of integers corresponding to the number of beats each note lasts.

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map the musical notes to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values of the notes
    beats = []

    # Iterate over the notes and their indices
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it is, append its beat value to the list
            beats.append(note_beats['o'])
        # Check if the current note is a half note or a quarter note
        elif notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it is, append its beat value to the list and skip the next note (the '|')
            beats.append(note_beats['o|'])
            i += 1
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it is, append its beat value to the list and skip the next note (the '|')
            beats.append(note_beats['.|'])
            i += 1
        i += 1

    # Return the list of beat values
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```