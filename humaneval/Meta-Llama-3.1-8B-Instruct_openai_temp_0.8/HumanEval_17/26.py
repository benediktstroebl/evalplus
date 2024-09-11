```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    The legend for the notes is:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    music_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Use a list comprehension to look up the beats for each note and return the result
    return [music_map[note] for note in notes]

# Example usage:
print(parse_music('o o|.| o| o|.|..|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. The function uses a dictionary `music_map` to map each note type to its corresponding beat duration. It then splits the input string into individual notes and uses a list comprehension to look up the beats for each note. The result is a list of integers representing the number of beats each note lasts.