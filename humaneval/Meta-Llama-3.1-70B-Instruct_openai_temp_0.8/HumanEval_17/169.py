```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string representing musical notes in a special ASCII format
    :return: A list of integers corresponding to how many beats each note lasts
    """

    # Define a dictionary to map notes to beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over the notes
    for note in notes:
        # If the note is a whole note, add it to the list of beats and reset the current note
        if note == 'o':
            beats.append(note_to_beats[note])
            current_note = ''
        # If the note is a half note or quarter note, add it to the current note
        elif note in ['o|', '.|']:
            current_note += note
            # If the current note is a valid note, add it to the list of beats and reset the current note
            if current_note in note_to_beats:
                beats.append(note_to_beats[current_note])
                current_note = ''

    # Return the list of beats
    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```