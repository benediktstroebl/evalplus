```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    The legend is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat
    """
    mapping = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    for note in music_string.split():
        if note in mapping:
            result.append(mapping[note])
    return result


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. It uses a dictionary `mapping` to map each note to its corresponding duration. The function splits the input string into individual notes, looks up their durations in the mapping, and appends the durations to the result list. Finally, it returns the result list. The example usage at the end demonstrates how to use the function to parse a string of musical notes.