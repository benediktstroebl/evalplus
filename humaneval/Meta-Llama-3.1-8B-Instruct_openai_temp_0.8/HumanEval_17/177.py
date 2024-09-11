### Music Note Parser
#### A Python script to parse musical notes in a special ASCII format

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return
    a list of integers corresponding to how many beats each note lasts.

    The legend for the notes is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes in the special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Use a list comprehension to create a list of beats for each note
    beats = [note_beats[note] for note in notes]
    
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes in the special ASCII format and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map each note to its corresponding beat duration, and then uses a list comprehension to create the list of beats. The script includes a test case to demonstrate the function's usage.