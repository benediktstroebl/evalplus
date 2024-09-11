```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map notes to their corresponding beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats of each note
    beats = []

    # Split the music string into individual notes
    notes = music_string.split()

    # Iterate over each note in the music string
    for note in notes:
        # Append the beats of the current note to the beats list
        beats.append(note_to_beats[note])

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses the notes to determine their corresponding beats, and returns a list of integers representing the beats of each note. The function uses a dictionary to map each note to its corresponding beats. The script then tests the function with the provided example.