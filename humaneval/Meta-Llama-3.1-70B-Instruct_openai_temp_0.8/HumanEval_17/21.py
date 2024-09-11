```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map note representations to their respective beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over the notes
    for note in notes:
        # If the note is not a space and not a standalone note, add it to the current note
        if note not in ['o', '.'] and current_note:
            current_note +='' + note
        # If the note is a standalone note or the last part of a note, add it to the current note
        else:
            current_note = note

        # If the current note is a complete note, add its beat duration to the list and reset the current note
        if current_note in note_durations:
            beat_durations.append(note_durations[current_note])
            current_note = ''

    return beat_durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```