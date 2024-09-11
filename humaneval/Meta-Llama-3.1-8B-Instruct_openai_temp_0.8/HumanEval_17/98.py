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
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    music_list = music_string.split()
    result = []
    
    # Iterate over the music list and append the note length to the result list
    for note in music_list:
        result.append(note_lengths[note])
    
    return result

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format as an input, and returns a list of integers corresponding to how many beats each note lasts. The function uses a dictionary to map each note to its corresponding length, splits the input string into a list of notes, and then iterates over the list to append the note length to the result list. The script also includes a test case to demonstrate the function's usage.