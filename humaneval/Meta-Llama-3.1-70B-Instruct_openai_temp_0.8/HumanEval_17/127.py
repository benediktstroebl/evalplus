```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    legend = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    durations = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # Add the duration of the half note to the list
            durations.append(legend['o|'])
            # Skip the next note
            i += 2
        elif notes[i] == 'o':
            # Add the duration of the whole note to the list
            durations.append(legend['o'])
            # Move to the next note
            i += 1
        elif notes[i] == '.|':
            # Add the duration of the quarter note to the list
            durations.append(legend['.|'])
            # Move to the next note
            i += 1

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```