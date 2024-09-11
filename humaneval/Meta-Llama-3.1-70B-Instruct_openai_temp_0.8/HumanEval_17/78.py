```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """

    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note in the input string
    for note in notes:
        # Check if the note is in the dictionary
        if note in note_beats:
            # If the note is in the dictionary, append its beats to the list
            beats.append(note_beats[note])
        elif note == 'o':  # special case for whole note
            beats.append(4)
        else:
            # If the note is not in the dictionary, raise a ValueError
            raise ValueError(f"Unknown note: {note}")

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```