```markdown
### Music Note Parser

This script takes a string of musical notes in a special ASCII format and returns a list of integers
representing the duration of each note in beats.

#### Legend
- `'o'`: whole note, lasts four beats
- `'o|'`: half note, lasts two beats
- `'.|'`: quarter note, lasts one beat
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the duration of each note.

    Args:
    music_string (str): A string of musical notes in the special ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note in beats.
    """
    note_durations = {'o': 4, 'o|': 2, '.|': 1}
    return [note_durations[note] for note in music_string.split()]

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

You can run this script to see the output. It uses a dictionary to map each note to its corresponding duration, and then uses a list comprehension to parse the input string and return the list of durations.