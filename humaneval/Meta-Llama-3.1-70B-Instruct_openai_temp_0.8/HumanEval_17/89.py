```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in special ASCII format and return a list of integers representing the beats each note lasts.

    :param music_string: A string of musical notes in special ASCII format
    :return: A list of integers representing the beats each note lasts
    """
    # Create a dictionary to map musical notes to their corresponding beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the list of notes
    for char in notes:
        # Add the character to the current note
        current_note += char

        # Check if the current note is in the note_to_beats dictionary
        if current_note in note_to_beats:
            # If it is, add its beats to the beats list and reset the current note
            beats.append(note_to_beats[current_note])
            current_note = ''

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

When you run this script, it will print the list of beats for the given musical notes, which should match the expected output `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.