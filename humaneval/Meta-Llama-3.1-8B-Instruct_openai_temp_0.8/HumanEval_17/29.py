```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the beat duration of each note.

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_durations = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Iterate over each note
    for note in notes:
        # Append the duration of the note to the result list
        result.append(note_durations[note])
    
    return result

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. It uses a dictionary to map the note symbols to their respective durations. The function splits the input string into individual notes, and then iterates over each note, appending its duration to the result list.