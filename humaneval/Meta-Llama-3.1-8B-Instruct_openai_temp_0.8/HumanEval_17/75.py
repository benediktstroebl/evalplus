### Musical Note Parser
#### Problem Description
Parse a musical note string and return a list of integers representing the number of beats each note lasts.

#### Code
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a musical note string and return a list of integers representing the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = []
    for note in music_string.split():
        beats.append(note_beats[note])
    
    return beats


# Example usage
if __name__ == "__main__":
    music_string = 'o o|.| o| o|.|.|.|.| o o'
    beats = parse_music(music_string)
    print(beats)
```

#### Explanation
This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format. It uses a dictionary to map each note type to its corresponding number of beats. The function splits the input string into individual notes, looks up each note in the dictionary, and appends its beats to a list. The function returns this list of beats. The example usage demonstrates how to use this function with a musical note string.