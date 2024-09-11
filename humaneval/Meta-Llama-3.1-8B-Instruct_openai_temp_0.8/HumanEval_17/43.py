```markdown
### Music Note Parser

This script takes a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts.
#### Code
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parses a string of musical notes in ASCII format and returns a list of integers representing the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    note_duration = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    music_list = music_string.split()
    result = []

    for note in music_list:
        result.append(note_duration.get(note, 0))  # if note is not found, append 0

    return result


# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```
#### Explanation

*   We define a dictionary `note_duration` to map each note type to its corresponding duration in beats.
*   The `parse_music` function takes a string of musical notes as input, splits it into a list of individual notes, and initializes an empty list `result` to store the note durations.
*   We iterate over each note in the list and append its duration to the `result` list using the `note_duration` dictionary. If a note is not found in the dictionary, we append 0 to the `result` list.
*   Finally, we return the `result` list, which contains the durations of all notes in the input string.