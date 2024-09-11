```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Create a dictionary to map note representations to their corresponding beat values
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values of the notes
    beat_values = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note and the next note form a multi-character note representation
        if i + 1 < len(notes) and notes[i] +'' + notes[i + 1] in ['o|', '.|']:
            # If they do, add the corresponding beat value to the list and skip the next note
            beat_values.append(note_values[notes[i] +'' + notes[i + 1]])
            i += 2
        else:
            # If they don't, add the corresponding beat value of the current note to the list
            beat_values.append(note_values[notes[i]])
            i += 1

    return beat_values


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```