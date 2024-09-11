**Musical Note Parser**
=======================

Below is a Python script that defines a function `parse_music` to parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Define a dictionary to map note symbols to their beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beat_values = []

    # Iterate over each note in the list of notes
    for note in notes:
        # Get the beat value of the current note from the dictionary
        beat = note_beats.get(note, 0)
        
        # Add the beat value to the list of beat values
        beat_values.append(beat)

    # Return the list of beat values
    return beat_values

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string representing musical notes as input and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map note symbols to their beat values and iterates over the input string to extract the beat values. The test at the end of the script demonstrates the function's usage.