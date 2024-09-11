```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
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
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the notes
    for char in notes:
        # Add the character to the current note
        current_note += char

        # If the current note is in the note_beats dictionary, add its beat value to the beats list
        if current_note in note_beats:
            beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''

    # Return the list of beat values
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```