### Music Note Parser
#### Problem Description
This script takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    note_values = {
        'o': 4,  # whole note, lasts four beats
        'o|': 2,  # half note, lasts two beats
        '.|': 1   # quarter note, lasts one beat
    }

    notes = music_string.split()
    beats = [note_values[note] for note in notes]

    return beats

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
#### Explanation
This script defines a dictionary `note_values` to map the note ASCII characters to their corresponding beat values. It then splits the input string into a list of notes using the `split` method, and uses a list comprehension to create a new list where each note is replaced by its corresponding beat value. The resulting list is returned by the function.