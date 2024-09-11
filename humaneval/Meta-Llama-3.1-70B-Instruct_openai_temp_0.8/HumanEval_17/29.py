Here is a self-contained Python script that solves the problem:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to how many beats a note lasts.

    :param music_string: A string of musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Define a dictionary to map each note symbol to its corresponding duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    durations = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it's a half note, add its duration to the list and skip the next note
            durations.append(note_durations['o|'])
            i += 2
        elif notes[i] == 'o':
            # If it's a whole note, add its duration to the list
            durations.append(note_durations['o'])
            i += 1
        # Check if the current note is a quarter note
        elif notes[i] == '.|':
            # If it's a quarter note, add its duration to the list
            durations.append(note_durations['.|'])
            i += 1

    # Return the list of note durations
    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers representing the duration of each note. It uses a dictionary to map each note symbol to its corresponding duration, splits the input string into individual notes, and then iterates over each note to determine its duration. The function handles whole notes, half notes, and quarter notes, and returns the list of note durations.