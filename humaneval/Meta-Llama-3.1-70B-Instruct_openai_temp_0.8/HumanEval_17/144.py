```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes in the format 'o', 'o|', or '.|' separated by spaces.
    :return: A list of integers representing the duration of each note in beats.
    """
    # Create a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note and append its duration to the list
    for note in notes:
        # Check if the note is in the dictionary and append its duration
        if note in note_durations:
            durations.append(note_durations[note])
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {note}")

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```