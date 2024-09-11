```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to the beats of each note
    """
    # Define a dictionary to map note representations to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an index to keep track of the current position in the notes list
    i = 0

    # Iterate over the notes
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it is, add its beats to the list and move to the next note
            beats.append(note_beats['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i] == 'o|' or notes[i] == '.|':
            # If it is, add its beats to the list and move to the next note
            beats.append(note_beats[notes[i]])
            i += 1

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script works by splitting the input string into individual notes, then iterating over these notes. It uses a dictionary to map each note representation to its corresponding beats, and it adds these beats to a list. Finally, it returns this list.

Please note that this script assumes that the input string is well-formed and does not contain any invalid notes. If the input string may contain invalid notes, you should add error checking code to handle this.