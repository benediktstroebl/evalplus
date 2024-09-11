### Music Note Parser
#### Problem Description
Parse a string of musical notes in a special ASCII format and return a list of integers representing the number of beats each note lasts.

#### Solution
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in the following format:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.
    """
    note_duration = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    result = []
    
    # Iterate over each note in the music list
    for note in music_list:
        # Append the duration of the note to the result list
        result.append(note_duration[note])
        
    # Return the result list
    return result

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes as input, splits the string into individual notes, looks up the duration of each note in a dictionary, and returns a list of integers representing the number of beats each note lasts. The example usage at the end demonstrates how to use this function with the provided test case.