```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return 
    a list of integers corresponding to how many beats each note lasts.

    The legend is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map note patterns to their corresponding beat values
    note_values = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to parse each note and append its value to the result list
    return [note_values[note] for note in notes]

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes as input, 
parses it, and returns a list of integers corresponding to how many beats each note lasts. The function 
uses a dictionary to map note patterns to their corresponding beat values. It then splits the input string 
into individual notes, uses a list comprehension to parse each note and append its value to the result list. 
Finally, it tests the function with the provided example.