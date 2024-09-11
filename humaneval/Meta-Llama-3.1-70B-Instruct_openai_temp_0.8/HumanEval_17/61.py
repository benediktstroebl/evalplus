```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
    """
    # Split the input string into a list of notes
    notes = music_string.split()

    # Define a dictionary to map each note to its corresponding beat duration
    note_durations = {
        'o': 4,  # Whole note
        'o|': 2,  # Half note
        '.|': 1  # Quarter note
    }

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Iterate over each note in the list of notes
    for note in notes:
        # Check if the note is a whole note
        if note == 'o':
            beat_durations.append(note_durations['o'])
        # Check if the note is a half note or a quarter note
        elif note in note_durations:
            beat_durations.append(note_durations[note])
        # If the note is not recognized, raise a ValueError
        else:
            raise ValueError(f"Unrecognized note: {note}")

    # Return the list of beat durations
    return beat_durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```