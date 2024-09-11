```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the number of beats each note lasts.
    """

    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
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

    # Iterate over each character in the notes
    for char in notes:
        # If the character is not a space, add it to the current note
        if char!='':
            current_note += char
        # If the current note is in the note_beats dictionary, add its beats to the list
        if current_note in note_beats:
            beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, the initial implementation of the notes splitting is wrong as it does not correctly separate notes. Here is the correct implementation.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the number of beats each note lasts.
    """

    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is not a space, add it to the current note
        if char!='':
            current_note += char
        # If the current note is in the note_beats dictionary, add its beats to the list
        if current_note in note_beats:
            beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, this does not handle 'o' that is part of 'o|'. We should modify the function to handle this.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers corresponding to the number of beats each note lasts.
    """

    #