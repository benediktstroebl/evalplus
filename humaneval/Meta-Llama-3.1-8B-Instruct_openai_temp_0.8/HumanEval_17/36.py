### Musical Note Parser
#### Parse musical notes from a string and return the duration of each note in beats

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse musical notes from a string and return the duration of each note in beats.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the duration of each note in beats.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map note types to their durations
    note_durations = {
        'o': 4,  # whole note lasts four beats
        'o|': 2,  # half note lasts two beats
        '.|': 1  # quarter note lasts one beat
    }

    # Initialize an empty list to store the note durations
    note_durations_list = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the duration of the note to the list
        note_durations_list.append(note_durations[note])

    # Return the list of note durations
    return note_durations_list

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes as input, and returns a list of integers corresponding to the duration of each note in beats. The function uses a dictionary to map note types to their durations, and then iterates over the input string to populate the output list. The example usage at the end demonstrates how to call the function with a sample input string.