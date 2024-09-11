```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the duration of each note.

    The string format is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes in the specified format.

    Returns:
        List[int]: A list of integers representing the duration of each note.
    """
    durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the note durations
    result = []
    
    # Iterate over each note
    for note in notes:
        # Append the duration of the current note to the result list
        result.append(durations[note])
    
    # Return the list of note durations
    return result

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map the note formats to their respective durations, and then iterates over each note in the input string to extract its duration. Finally, the function returns the list of note durations.