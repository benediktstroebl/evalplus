```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer corresponds to the number of beats a note lasts.

    :param music_string: A string of musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note and the next note form a half note or a quarter note
        if i + 1 < len(notes) and notes[i] == 'o' and notes[i + 1] == '|':
            # If they form a half note, add the beats of a half note to the list and skip the next note
            beats.append(note_beats['o|'])
            i += 2
        elif i + 1 < len(notes) and notes[i] == '.' and notes[i + 1] == '|':
            # If they form a quarter note, add the beats of a quarter note to the list and skip the next note
            beats.append(note_beats['.|'])
            i += 2
        else:
            # If the current note is a whole note, add the beats of a whole note to the list
            beats.append(note_beats['o'])
            i += 1

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```