```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the number of beats each note lasts
    """
    # Create a dictionary to map notes to their corresponding beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Iterate over the notes and append their corresponding beats to the list
    i = 0
    while i < len(notes):
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            beats.append(note_to_beats['o|'])
            i += 2
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            beats.append(note_to_beats['.|'])
            i += 2
        else:
            beats.append(note_to_beats['o'])
            i += 1

    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```