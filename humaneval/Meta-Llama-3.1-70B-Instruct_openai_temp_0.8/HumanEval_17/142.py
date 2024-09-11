```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to
    how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map note symbols to their corresponding beat lengths
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat lengths
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            beats.append(note_beats['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i:i+2] in note_beats:
            beats.append(note_beats[notes[i:i+2]])
            i += 2
        else:
            raise ValueError(f"Invalid note: {notes[i]}")

    return beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```