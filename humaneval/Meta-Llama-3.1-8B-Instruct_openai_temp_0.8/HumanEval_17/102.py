```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in ASCII format and returns a list of integers representing
    the number of beats each note lasts.

    The legend for the notes is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map musical notes to their beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the beat duration of the note to the list
        beat_durations.append(note_durations[note])

    # Return the list of beat durations
    return beat_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map musical notes to their beat durations and then splits the input string into individual notes, iterating over each note to append its beat duration to the list. The script includes a test case at the end to demonstrate the function's usage.