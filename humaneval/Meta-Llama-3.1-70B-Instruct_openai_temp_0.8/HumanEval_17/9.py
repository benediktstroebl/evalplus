```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string, and returns a list of integers corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to the number of beats each note lasts.
    """

    # Define a dictionary to map musical notes to their corresponding beats
    beats_map = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note in the notes list
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o':
            # Append the beats for the whole note to the beats list
            beats.append(beats_map['o'])
            i += 1
        # Check if the note is a half note or a quarter note
        elif notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # Append the beats for the half note to the beats list
            beats.append(beats_map['o|'])
            i += 2
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            # Append the beats for the quarter note to the beats list
            beats.append(beats_map['.|'])
            i += 2
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {notes[i]}")

    # Return the list of beats
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```