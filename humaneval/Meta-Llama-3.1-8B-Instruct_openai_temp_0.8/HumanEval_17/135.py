```markdown
### Music Note Parser

This Python script parses a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    Example:
    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Iterate over each note in the input string
    for note in notes:
        # Append the beat value of the current note to the result list
        result.append(note_beats[note])
    
    return result

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Explanation

This script uses a dictionary `note_beats` to map each musical note to its corresponding beat value. It then splits the input string into individual notes, iterates over each note, and appends its beat value to the result list. The function finally returns the list of beat values.
```