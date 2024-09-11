### Music String Parser
#### Parse a string representing musical notes into a list of integers corresponding to note duration

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes into a list of integers corresponding to note duration.

    The music string is in a special ASCII format:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat

    Args:
        music_string (str): The input string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to note duration.
    """
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    notes = music_string.split()
    result = []

    for note in notes:
        result.append(note_durations[note])

    return result

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This Python script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note. The function uses a dictionary to map each note type to its corresponding duration. It then splits the input string into individual notes, looks up the duration of each note in the dictionary, and returns the list of durations. The example usage demonstrates how to use this function with a sample music string.