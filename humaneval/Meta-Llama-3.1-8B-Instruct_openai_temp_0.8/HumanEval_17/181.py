```python
from typing import List
import re

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    
    # Create a dictionary to map notes to their beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Use regular expression to find all notes in the string
    notes = re.findall(r'o(o)?\|?\.\?', music_string)
    
    # Use list comprehension to create a list of beats for each note
    beats = [note_beats[note] for note in notes]
    
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script uses the `re` module to find all notes in the string using regular expressions. It then uses a list comprehension to create a list of beats for each note. The `note_beats` dictionary maps each note to its corresponding beats. The function returns this list of beats.