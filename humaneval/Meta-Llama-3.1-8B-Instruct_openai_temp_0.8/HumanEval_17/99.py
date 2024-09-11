### Music Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to the number of beats each note lasts.

    The string should use the following notation:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map note strings to their corresponding beat values
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to convert each note to its corresponding beat value
    beat_values = [note_beats[note] for note in notes]

    return beat_values

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script uses a dictionary to map each note string to its corresponding beat value, and then uses a list comprehension to convert each note in the input string to its corresponding beat value. The resulting list of beat values is then returned by the `parse_music` function.