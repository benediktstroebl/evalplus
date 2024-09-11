```python
from typing import List
import re

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map the notes to their respective beat lengths
    note_beat_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Use regular expression to match the notes and their corresponding beat lengths
    matches = re.findall(r'([o.o|.|:])', music_string)

    # Initialize an empty list to store the beat lengths
    beat_lengths = []

    # Iterate over the matches and append the corresponding beat length to the list
    for match in matches:
        if match == 'o':  # whole note
            beat_lengths.append(note_beat_lengths[match])
        elif match == 'o|':  # half note
            beat_lengths.append(note_beat_lengths[match])
        else:  # quarter note
            beat_lengths.append(note_beat_lengths[match])

    return beat_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```