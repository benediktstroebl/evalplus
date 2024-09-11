### Musical Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_dict = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary mapping note types to beat duration
    notes = music_string.split()  # Split the input string into individual notes
    beat_durations = [note_dict[note] for note in notes]  # Create a list of beat durations
    return beat_durations  # Return the list of beat durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map note types to their corresponding beat durations, splits the input string into individual notes, and then creates a list of beat durations. Finally, the script includes an example usage of the function.