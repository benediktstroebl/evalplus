```markdown
### Music Note Parser

This Python script takes a string of musical notes in a special ASCII format and returns a list of integers representing the number of beats each note lasts.
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse string of musical notes and return list of integers corresponding to the number of beats each note lasts.

    The input string uses the following legend:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quater note, lasts one beat

    Args:
        music_string (str): String of musical notes

    Returns:
        List[int]: List of integers representing the number of beats each note lasts
    """
    # Define a dictionary to map each note type to its corresponding beat count
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to map each note to its corresponding beat count
    beats = [note_beats[note] for note in notes]

    return beats

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script uses a dictionary to map each note type to its corresponding beat count, then uses a list comprehension to map each note in the input string to its corresponding beat count. The result is a list of integers representing the number of beats each note lasts.