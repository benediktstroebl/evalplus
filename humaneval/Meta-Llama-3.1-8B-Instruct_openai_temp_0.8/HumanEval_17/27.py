### Music Note Parser
#### Parse musical notes from a string and return their corresponding beat lengths

```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to the beat lengths.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the beat lengths of each note.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    music_list = music_string.split()
    beat_lengths = [note_lengths[note] for note in music_list]
    return beat_lengths


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes as input, splits it into individual notes, and then uses a dictionary to map each note to its corresponding beat length. The beat lengths are then returned as a list of integers. The script also includes an example usage of the `parse_music` function.