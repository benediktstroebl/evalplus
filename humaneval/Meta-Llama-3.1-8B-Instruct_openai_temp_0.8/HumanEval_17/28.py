### Music Note Parser
#### Overview
This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    notes = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quater note
    }

    # Split the input string into individual notes
    notes_list = music_string.split()

    # Initialize an empty list to store the result
    result = []

    # Iterate over each note in the list
    for note in notes_list:
        # Append the duration of the current note to the result list
        result.append(notes[note])

    # Return the result list
    return result

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a dictionary `notes` that maps each musical note to its duration. It then splits the input string into individual notes, iterates over each note, and appends its duration to the result list. Finally, it returns the result list.