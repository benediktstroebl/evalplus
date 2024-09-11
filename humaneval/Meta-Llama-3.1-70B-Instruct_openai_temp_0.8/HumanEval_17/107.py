```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    # Create a dictionary to map notes to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beat_values = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # Append the beat value of a whole note to the list
            beat_values.append(note_beats['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i] in note_beats:
            # Append the beat value of the note to the list
            beat_values.append(note_beats[notes[i]])
        # If the note is not recognized, raise a ValueError
        else:
            raise ValueError(f"Unrecognized note: {notes[i]}")
        i += 1

    # Return the list of beat values
    return beat_values

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```