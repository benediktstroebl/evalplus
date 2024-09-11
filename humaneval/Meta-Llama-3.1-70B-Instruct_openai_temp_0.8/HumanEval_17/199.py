```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes in a special ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map the musical notes to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values of the notes
    beat_values = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each note in the input string
    for note in notes:
        # If the note is 'o', it could be either a whole note or the start of a half note
        if note == 'o':
            # Add the note to the current note
            current_note += note
        # If the note is '|' or '.', it must be the end of a note
        elif note in ['|', '.']:
            # Add the note to the current note
            current_note += note
            # Get the beat value of the current note from the dictionary
            beat_values.append(note_beats[current_note])
            # Reset the current note
            current_note = ''
        # If the note is '.|', it's a quarter note and we can process it immediately
        elif note == '.|':
            beat_values.append(note_beats[note])

    # Return the list of beat values
    return beat_values


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```