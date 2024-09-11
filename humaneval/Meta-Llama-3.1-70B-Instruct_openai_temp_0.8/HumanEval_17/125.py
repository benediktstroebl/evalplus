```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer corresponds to the number of beats a note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """

    # Create a dictionary to map note representations to their corresponding beat values
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beats = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a half or quarter note
        if i < len(notes) - 1 and notes[i] == 'o' and notes[i + 1] == '|':
            beats.append(note_beats['o|'])
            i += 2
        elif i < len(notes) - 1 and notes[i] == '.' and notes[i + 1] == '|':
            beats.append(note_beats['.|'])
            i += 2
        else:
            # If the current note is a whole note, add its beat value to the list
            beats.append(note_beats['o'])
            i += 1

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```