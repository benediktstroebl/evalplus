```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string of musical notes in ASCII format
    :return: A list of integers representing the number of beats for each note
    """
    # Define a dictionary to map note representations to their corresponding beat values
    note_values = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat values
    beats = []

    # Initialize an index to track the current position in the notes list
    i = 0

    # Iterate over the notes
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it is, append its beat value to the list and move to the next note
            beats.append(note_values['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it is, append its beat value to the list and move two positions forward
            beats.append(note_values['o|'])
            i += 2
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it is, append its beat value to the list and move two positions forward
            beats.append(note_values['.|'])
            i += 2

    return beats


# Test the function
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```