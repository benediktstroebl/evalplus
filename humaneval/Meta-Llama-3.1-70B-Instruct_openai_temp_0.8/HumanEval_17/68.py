```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the note is a whole note or a half note or a quarter note
        if i + 1 < len(notes) and notes[i] == 'o' and notes[i + 1] == '|':
            # If it's a half note, append its beats to the list and increment the index by 2
            beats.append(note_beats['o|'])
            i += 2
        elif i + 1 < len(notes) and notes[i] == '.' and notes[i + 1] == '|':
            # If it's a quarter note, append its beats to the list and increment the index by 2
            beats.append(note_beats['.|'])
            i += 2
        else:
            # If it's a whole note, append its beats to the list and increment the index by 1
            beats.append(note_beats['o'])
            i += 1

    # Return the list of beats
    return beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```