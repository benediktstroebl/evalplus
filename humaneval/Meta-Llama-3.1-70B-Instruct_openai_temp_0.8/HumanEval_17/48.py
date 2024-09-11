```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Define a dictionary to map note symbols to their corresponding beat duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it's a whole note, append its beat duration to the list
            beat_durations.append(note_durations['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif i + 1 < len(notes) and notes[i] + notes[i+1] in note_durations:
            # If it's a half note or a quarter note, append its beat duration to the list
            beat_durations.append(note_durations[notes[i] + notes[i+1]])
            i += 2
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {notes[i]}")

    # Return the list of beat durations
    return beat_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format, parses the string and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map note symbols to their corresponding beat duration and splits the input string into individual notes. It then iterates over each note, checks its type and appends its beat duration to the list. The function raises a ValueError if it encounters an unrecognized note.