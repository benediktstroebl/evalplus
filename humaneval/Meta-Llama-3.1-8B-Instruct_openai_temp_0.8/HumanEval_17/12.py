### Music Note Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    The input string uses the following notation:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string of musical notes

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts
    """
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    beats = [note_map[note] for note in notes]
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a string of musical notes as input, splits it into individual notes, and then maps each note to its corresponding number of beats using a dictionary. The function finally returns a list of integers representing the number of beats each note lasts.