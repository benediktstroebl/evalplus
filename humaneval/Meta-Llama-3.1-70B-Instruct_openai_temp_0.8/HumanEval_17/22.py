```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes in a special ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map the musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            beats.append(note_beats['o|'])
            i += 2
        # Check if the note is a half note or a quarter note
        elif notes[i] + '|' in note_beats:
            beats.append(note_beats[notes[i] + '|'])
            i += 2
        # If the note is not followed by '|', it's a whole note
        else:
            beats.append(note_beats['o'])
            i += 2

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes and returns a list of integers representing the number of beats each note lasts. It uses a dictionary to map the musical notes to their corresponding beats and then splits the input string into a list of notes. It then iterates over each note in the list, checks its type, and appends its beats to the result list. The function is tested with the example input `'o o|.| o| o|.|.|.|.| o o'`.

However, the above function does not work correctly for the example input as it only checks for 'o' and '.|', it does not correctly parse the musical notes.

Here is a corrected version of the function:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes in a special ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map the musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the input string
    for char in music_string +'':
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the note is not empty, append its beats to the result list
            if note:
                # If the note is followed by '|', remove the '|' and append its beats