```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses the string and returns a list of integers corresponding to how many beats each note lasts.

    The legend for notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string of musical notes in ASCII format
    :return: A list of integers representing the duration of each note in beats
    """

    # Create a dictionary to map notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the durations of notes
    note_beats = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the list
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o':
            # Append the duration of the whole note to the result list
            note_beats.append(note_durations['o'])
        # Check if the note is a half note or a quarter note
        elif notes[i] in ['o|', '.|']:
            # Append the duration of the note to the result list
            note_beats.append(note_durations[notes[i]])
        # If the note is not recognized, raise a ValueError
        else:
            raise ValueError(f"Unrecognized note: {notes[i]}")
        
        # Move to the next note
        i += 1

    # Return the list of note durations
    return note_beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Expected output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```