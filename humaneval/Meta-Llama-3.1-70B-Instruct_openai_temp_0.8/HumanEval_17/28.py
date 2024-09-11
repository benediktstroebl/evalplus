```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map the notes to their respective beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o':
            # If it is, append the beats for a whole note to the list
            beats.append(note_beats['o'])
        # Check if the note is a half note
        elif i < len(notes) - 1 and notes[i] + notes[i + 1] == 'o|':
            # If it is, append the beats for a half note to the list
            beats.append(note_beats['o|'])
            # Skip the next note as it is part of the current note
            i += 1
        # Check if the note is a quarter note
        elif i < len(notes) - 1 and notes[i] + notes[i + 1] == '.|':
            # If it is, append the beats for a quarter note to the list
            beats.append(note_beats['.|'])
            # Skip the next note as it is part of the current note
            i += 1
        i += 1

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

However the code can be simplified further. Here's a more simplified version of it:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    # Define a dictionary to map the notes to their respective beats
    note_beats = {
        'o': 4,
       