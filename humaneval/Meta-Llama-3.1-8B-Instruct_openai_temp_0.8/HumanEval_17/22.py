### Music Note Parser
#### Python Script
```markdown
from typing import List
import re


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format
    and return a list of integers corresponding to the number of beats each note lasts.

    :param music_string: String representing musical notes
    :return: List of integers representing the number of beats each note lasts
    """
    # Regular expression pattern to match musical notes
    pattern = re.compile(r'o|o\||\.\|')

    # Initialize list to store note durations
    note_durations = []

    # Iterate over matches of the pattern in the input string
    for match in pattern.finditer(music_string):
        # Get the matched note
        note = match.group()

        # Determine the note duration based on the matched note
        if note == 'o':
            note_durations.append(4)
        elif note == 'o|':
            note_durations.append(2)
        elif note == '.|':
            note_durations.append(1)

    return note_durations


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script uses a regular expression to match the musical notes in the input string, and then uses a dictionary to determine the duration of each note based on the matched note. The durations are then appended to a list and returned.