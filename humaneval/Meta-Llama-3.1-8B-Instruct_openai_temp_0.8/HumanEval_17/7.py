Here is a Python script that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the beats for each note.
    """
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats
    beats = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the beats for the current note to the list
        beats.append(note_beats[note])

    # Return the list of beats
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string representing musical notes as input and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map notes to their corresponding beats, and then iterates over the input string to append the beats for each note to the list. The example usage at the end shows how to use the function to parse a string of musical notes.