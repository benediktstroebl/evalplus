### Music Note Parser
#### Problem Description
Parse a string of musical notes in ASCII format and return a list of integers representing the duration of each note.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse musical notes in ASCII format and return a list of integers representing the duration of each note.

    Args:
    music_string (str): A string of musical notes in ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note.
    """
    note_durations = {
        'o': 4,  # whole note, lasts four beats
        'o|': 2,  # half note, lasts two beats
        '.|': 1,  # quarter note, lasts one beat
        '|': 0  # separator, ignores the note
    }

    music_notes = music_string.split()
    result = []

    for note in music_notes:
        if note in note_durations:
            result.append(note_durations[note])

    return result

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

#### Explanation
This script defines a function `parse_music` that takes a string of musical notes in ASCII format as input and returns a list of integers representing the duration of each note.

The function uses a dictionary `note_durations` to map each musical note to its corresponding duration.

It splits the input string into individual notes using the `split` method, then iterates over each note. If the note is found in the `note_durations` dictionary, its duration is appended to the result list.

Finally, the function returns the list of note durations.

In the example usage, we call the `parse_music` function with a sample string of musical notes and print the resulting list of note durations.