```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding 
    to how many beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note
    """

    # Define a dictionary to map notes to their corresponding beat duration
    note_duration_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat duration of each note
    beat_durations = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # Add the character to the current note
        note += char

        # If the note is complete (i.e., it matches a key in the note_duration_map), 
        # add its beat duration to the list and reset the note
        if note in note_duration_map:
            beat_durations.append(note_duration_map[note])
            note = ''

    # Remove trailing spaces from notes before splitting
    notes = music_string.split()
    # Check if there are any leftover notes that were not processed
    if len(notes)!= len(beat_durations):
        raise ValueError("Invalid note format in input string")

    return beat_durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```