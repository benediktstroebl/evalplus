```python
from typing import List
from functools import reduce

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing 
    the number of beats each note lasts.

    Args:
    music_string (str): A string of musical notes in the format described above.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.

    Examples:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    
    # Define a dictionary to map note characters to their corresponding beats
    note_beats = {
        'o': 4, 
        'o|': 2, 
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Use a list comprehension to get the beats for each note
    beats = [note_beats[note] for note in notes]
    
    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary to map note characters to their corresponding beats, splits the input string into individual notes, and then uses a list comprehension to get the beats for each note. The function returns the list of beats. The script also includes a test case to demonstrate the function's behavior.