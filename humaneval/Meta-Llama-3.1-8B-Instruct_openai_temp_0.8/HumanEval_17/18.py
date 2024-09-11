```markdown
### Music Note Parser

This script takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = music_string.split()
    beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [beats[note] for note in notes]

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Explanation

This script defines a function `parse_music` that takes a string `music_string` representing musical notes in a special ASCII format. The function splits the input string into individual notes, and then uses a dictionary `beats` to map each note to its corresponding beat length. Finally, it returns a list of beat lengths corresponding to each note.

The script also includes an example usage of the `parse_music` function, which prints the list of beat lengths for the input string `'o o|.| o| o|.|.|.|.| o o'`.