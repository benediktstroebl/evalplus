```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    The legend is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map note characters to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats
    beats = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the list of notes
    for note in notes:
        # Append the beats corresponding to the current note to the list of beats
        beats.append(note_beats[note])

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map note characters to their corresponding beats, then splits the input string into individual notes and iterates over them to append their corresponding beats to the list. The script includes a test case at the end to demonstrate the function's usage.