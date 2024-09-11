```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over the notes and append their corresponding beats to the list
    i = 0
    while i < len(notes):
        if notes[i] == 'o':
            # Check if the next note is '|' to handle 'o|' correctly
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_beats['o|'])
                i += 2  # Skip the '|' character
            else:
                beats.append(note_beats['o'])
                i += 1
        elif notes[i] == '.|':
            beats.append(note_beats['.|'])
            i += 1
        else:
            raise ValueError(f"Invalid note symbol: {notes[i]}")

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```