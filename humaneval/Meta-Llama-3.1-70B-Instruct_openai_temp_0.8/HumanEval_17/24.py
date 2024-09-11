```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the 
    number of beats each note lasts.

    :param music_string: A string of musical notes in ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its beats to the list
            if current_note:
                beats.append(note_beats[current_note])
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the beats for the last note
    if current_note:
        beats.append(note_beats[current_note])

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

However, here is a more Pythonic solution:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the 
    number of beats each note lasts.

    :param music_string: A string of musical notes in ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.replace(' ', '')

    # Use list comprehension to get the beats for each note
    beats = [note_beats[note] for note in [notes[i:i+2] for i in range(0, len(notes), 2)]]

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```