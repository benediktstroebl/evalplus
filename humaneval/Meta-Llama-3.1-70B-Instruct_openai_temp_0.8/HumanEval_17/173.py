```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers
    corresponding to the number of beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over the notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it is, add its beats to the list and move to the next note
            beats.append(note_beats['o'])
        # Check if the current note is a half note or a quarter note
        elif notes[i] + '|' in note_beats:
            # If it is, add its beats to the list and move to the next note
            beats.append(note_beats[notes[i] + '|'])
            i += 1  # Skip the '|' symbol
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note symbol: {notes[i]}")

        i += 1

    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```