```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the number of beats each note lasts
    """

    # Create a dictionary to map notes to their corresponding beat values
    note_beat_values = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beat_values = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it's a whole note, append its beat value and skip the next note
            beat_values.append(note_beat_values['o'])
            i += 2
        elif notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it's a half note, append its beat value and skip the next note
            beat_values.append(note_beat_values['o|'])
            i += 2
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it's a quarter note, append its beat value and skip the next note
            beat_values.append(note_beat_values['.|'])
            i += 2
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {notes[i]}")
    
    return beat_values


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```