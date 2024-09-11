```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
    """

    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,  # Whole note lasts four beats
        'o|': 2,  # Half note lasts two beats
        '.|': 1  # Quarter note lasts one beat
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note in the list
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o':
            beats.append(note_beats['o'])
            i += 1
        # Check if the note is a half note or a quarter note
        elif notes[i] == 'o|' or notes[i] == '.|':
            beats.append(note_beats[notes[i]])
            i += 1
        # If the note is not recognized, raise a ValueError
        else:
            raise ValueError("Invalid note")

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map notes to their corresponding beats and splits the input string into a list of notes. It then iterates over each note, checks its type, and appends the corresponding number of beats to the list. Finally, it returns the list of beats. The script also includes a test case to demonstrate the function's usage.