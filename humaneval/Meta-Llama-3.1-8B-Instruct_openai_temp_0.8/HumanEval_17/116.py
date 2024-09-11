### Music Note Parser
#### A Python Script to Parse Musical Notes from ASCII Strings
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers
    representing the number of beats each note lasts.

    Available notes:
    - 'o' (whole note): lasts 4 beats
    - 'o|' (half note): lasts 2 beats
    - '.|' (quater note): lasts 1 beat

    Args:
        music_string (str): A string of musical notes in ASCII format

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts
    """
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note lengths
    note_lengths_list = []

    # Iterate over each note and add its length to the list
    for note in notes:
        if note in note_lengths:
            note_lengths_list.append(note_lengths[note])

    # Return the list of note lengths
    return note_lengths_list

# Example usage:
music_string = 'o o|.|. o| o|.|..|..|. o o'
print(parse_music(music_string))
# [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map each note to its corresponding length, splits the input string into individual notes, and then iterates over each note to add its length to the output list.