```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer corresponds to how many beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the beats of each note.
    """

    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the music string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it is, append its beats to the list
            beats.append(note_beats['o'])
            # Skip the next iteration since we've already processed the next note
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # If it is, append its beats to the list
            beats.append(note_beats[notes[i]])
        # If the current note is not a whole note, half note, or quarter note, raise an error
        else:
            raise ValueError(f"Invalid note: {notes[i]}")
        i += 1

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function called `parse_music` that takes a string of musical notes and returns a list of integers corresponding to the beats of each note. The function uses a dictionary to map notes to their corresponding beats, splits the input string into individual notes, and then iterates over each note to append its beats to the list.

However, the above function does not work correctly. We will be using another approach. 
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer corresponds to how many beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the beats of each note.
    """

    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build the current note
    note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the note is not empty, append its beats to the list
            if note:
                if note in note_beats:
                    beats.append(note_beats[note])
                else:
                    raise ValueError(f"Invalid note: {note}")
                # Reset the note
                note = ''
        else:
            # If the character is not a