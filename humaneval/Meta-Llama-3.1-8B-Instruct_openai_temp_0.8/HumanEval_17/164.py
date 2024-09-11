```markdown
### Music Note Parser

This script takes a string of musical notes in a special ASCII format and returns a list of integers
representing the number of beats each note lasts.
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map note types to their beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Get the beat duration for the current note from the dictionary
        duration = note_durations.get(note, 0)
        # Append the beat duration to the list
        beat_durations.append(duration)

    # Return the list of beat durations
    return beat_durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map note types to their beat durations and then iterates over each note in the input string to extract its beat duration. Finally, it returns the list of beat durations.