```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes and returns a list of integers
    corresponding to the number of beats each note lasts.

    The input string is in a special ASCII format where:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    notes = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes_list = music_string.split()

    # Initialize an empty list to store the beat counts
    beat_counts = []

    # Iterate over each note in the list
    for note in notes_list:
        # Append the beat count of the current note to the list
        beat_counts.append(notes[note])

    # Return the list of beat counts
    return beat_counts


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the number of beats each note lasts. It uses a dictionary to map note characters to their corresponding beat counts. The function splits the input string into individual notes, iterates over each note, and appends its beat count to a list. The list is then returned. The script also includes a test case to verify the function's correctness.