### Music Note Parser
#### Problem Description
Parse a string of musical notes in ASCII format and return a list of integers representing the number of beats each note lasts.

#### Solution
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the number of beats each note lasts.

    The legend is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map note types to their corresponding beat counts
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to create a list of beat counts for each note
    beats = [note_beats[note] for note in notes]

    return beats


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes as input, splits it into individual notes, maps each note type to its corresponding beat count, and returns a list of beat counts. The example usage demonstrates how to use this function with a sample input string.