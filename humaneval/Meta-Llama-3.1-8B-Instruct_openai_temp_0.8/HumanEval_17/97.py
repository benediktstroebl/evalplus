### Music Note Parser
#### Python Script to Parse Musical Notes

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats
    beats = []
    
    # Iterate over each note in the list of notes
    for note in notes:
        # Append the corresponding beats to the list
        beats.append(note_beats.get(note, 0))
    
    # Return the list of beats
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map notes to their corresponding beats and splits the input string into individual notes before iterating over them and appending their corresponding beats to a list. The function finally returns the list of beats. The example usage demonstrates how to call the function with a sample musical note string.