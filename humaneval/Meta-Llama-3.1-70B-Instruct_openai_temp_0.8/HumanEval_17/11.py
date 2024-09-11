```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the number of beats each note lasts
    """
    # Create a dictionary to map musical notes to their corresponding number of beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it is, add 4 beats to the list and skip the next character
            beats.append(note_to_beats['o'])
            i += 2
        # Check if the current note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # If it is, add the corresponding number of beats to the list
            beats.append(note_to_beats[notes[i]])
            i += 1
        # If the current note is not recognized, raise a ValueError
        else:
            raise ValueError(f"Unrecognized note: {notes[i]}")

    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```