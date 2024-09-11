```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map note symbols to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beats = []

    # Iterate over the notes and append their corresponding beat values to the list
    i = 0
    while i < len(notes):
        if notes[i] == 'o':
            # Check if the next note is '|' to handle 'o|' case
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_beats['o|'])
                i += 2
            else:
                beats.append(note_beats['o'])
                i += 1
        elif notes[i] == '.|':
            beats.append(note_beats['.|'])
            i += 1

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```