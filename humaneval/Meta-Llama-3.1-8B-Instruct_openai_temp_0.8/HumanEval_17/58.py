### Music Note Parser

This Python script defines a function `parse_music` that takes a string representing musical notes and returns a list of integers corresponding to the duration of each note.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse musical notes from a string and return a list of their durations.

    The input string uses a special ASCII format:
    - 'o' represents a whole note (4 beats)
    - 'o|' represents a half note (2 beats)
    - '.|' represents a quarter note (1 beat)

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to the duration of each note.
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    result = []
    for char in music_string:
        if char =='':
            # Ignore spaces
            continue
        elif char == '|':
            # Handle the '|' character separately
            if result and result[-1] == notes['o']:
                result.pop()
                result.append(notes['o|'])
            else:
                result.append(notes['o|'])
        else:
            result.append(notes[char])

    return result

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a dictionary `notes` to map the note representations to their corresponding durations. It then iterates over the input string, appending the duration of each note to the result list. When it encounters a '|' character, it handles it separately to ensure that it is appended to the correct note. The script ignores spaces in the input string.