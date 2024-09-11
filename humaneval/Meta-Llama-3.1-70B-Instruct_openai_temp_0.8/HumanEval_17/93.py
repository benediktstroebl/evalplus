```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """
    # Define a dictionary to map each note symbol to its corresponding duration in beats
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it's a whole note, append its duration to the list and move to the next note
            durations.append(note_durations['o'])
            i += 2
        # Check if the current note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # If it's a half note or a quarter note, append its duration to the list and move to the next note
            durations.append(note_durations[notes[i]])
            i += 1
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note symbol: {notes[i]}")

    # Return the list of note durations
    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```