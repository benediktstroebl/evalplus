```markdown
### Music Note Parser

This script parses a string of musical notes in a special ASCII format and returns a list of integers representing how many beats each note lasts.

#### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    music_dict = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quater note
    }
    music_list = music_string.split()
    beats_list = [music_dict[note] for note in music_list]
    return beats_list

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

#### Explanation

This script uses a dictionary to map each note type to its corresponding beat duration. It then splits the input string into individual notes, looks up each note in the dictionary, and returns a list of beat durations.

#### Output

When run with the example input `'o o|.| o| o|.|.|.|.| o o'`, this script will output `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.