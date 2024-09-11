```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    The string is in a special ASCII format:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Split the string into individual notes
    notes = music_string.split()
    
    # Create a dictionary to map each note to its duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    # Use a list comprehension to get the duration of each note
    durations = [note_durations[note] for note in notes]
    
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map each note to its duration and a list comprehension to get the duration of each note. The function is then tested with the provided example input.