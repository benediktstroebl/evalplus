```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats that the respective note lasts.

    The legend for the ASCII format is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string of musical notes in the special ASCII format
    :return: A list of integers, each representing the number of beats that the corresponding note lasts
    """

    # First, we define a dictionary that maps each note to its corresponding number of beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # We split the input string into individual notes
    notes = music_string.split()

    # Then, we initialize an empty list to store the number of beats for each note
    beats = []

    # We iterate over each note in the input string
    i = 0
    while i < len(notes):
        # If the note is a whole note, we add its beats to the list and move on to the next note
        if notes[i] == 'o':
            beats.append(note_beats['o'])
            i += 1
        # If the note is a half note or a quarter note, we add its beats to the list and move on to the next note
        elif notes[i:i+2] in note_beats:
            beats.append(note_beats[notes[i:i+2]])
            i += 2
        # If the note is not recognized, we raise a ValueError
        else:
            raise ValueError(f"Unrecognized note: {notes[i]}")

    # Finally, we return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```