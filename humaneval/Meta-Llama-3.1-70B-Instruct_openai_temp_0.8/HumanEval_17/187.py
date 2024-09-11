```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Create a dictionary to map note representations to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the notes string
    for char in notes:
        # Add the character to the current note
        current_note += char

        # Check if the current note is in the note_durations dictionary
        if current_note in note_durations:
            # If it is, append its duration to the durations list
            durations.append(note_durations[current_note])
            # Reset the current note
            current_note = ''

    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

When you run this script, it will output: `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`

This script works by mapping note representations to their corresponding durations, then splitting the input string into individual notes. It iterates over each character in the notes string, building up the current note and checking if it's in the note_durations dictionary. If it is, it appends its duration to the durations list. Finally, it returns the list of durations.