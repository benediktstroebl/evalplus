```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note
    """
    # Dictionary to map notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over the notes
    for note in notes:
        # If the note is not a whole note, it might be part of a longer note
        if note!= 'o':
            # Add the note to the current note
            current_note += note
            # If the current note is in the note_durations dictionary, it's a complete note
            if current_note in note_durations:
                # Add the duration of the current note to the durations list
                durations.append(note_durations[current_note])
                # Reset the current note
                current_note = ''
        else:
            # If the note is a whole note, it's a complete note
            # Add the duration of the whole note to the durations list
            durations.append(note_durations['o'])

    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map notes to their durations and splits the input string into notes. It then iterates over the notes, building up longer notes from shorter ones and adding their durations to the output list. The script includes a test case to demonstrate its usage.