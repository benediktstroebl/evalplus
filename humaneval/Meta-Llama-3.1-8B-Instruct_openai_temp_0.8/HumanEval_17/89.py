### Musical Note Parser
#### Python Script

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.

    Args:
    music_string (str): A string containing musical notes in the format 'o', 'o|', '.|'.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    """
    # Define a dictionary to map musical notes to their beat duration
    note_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Iterate over each note in the list
    for note in notes:
        # Append the duration of the current note to the list
        beat_durations.append(note_duration[note])

    # Return the list of beat durations
    return beat_durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in ASCII format and returns a list of integers corresponding to the number of beats each note lasts. The function splits the input string into individual notes, maps each note to its duration using a dictionary, and returns the list of beat durations.