```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the duration of each note.

    :param music_string: A string of musical notes in ASCII format
    :return: A list of integers representing the duration of each note
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    note_durations = []

    # Iterate over each note in the list of notes
    for note in notes:
        # Use a dictionary to map each note type to its corresponding duration
        note_types = {
            'o': 4,  # whole note
            'o|': 2,  # half note
            '.|': 1  # quarter note
        }

        # Check if the note is in the dictionary
        if note in note_types:
            # If it is, append its duration to the list of note durations
            note_durations.append(note_types[note])
        else:
            # If it's not, raise a ValueError with a descriptive error message
            raise ValueError(f"Invalid note type: {note}")

    # Return the list of note durations
    return note_durations


# Test the function with the provided example
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```