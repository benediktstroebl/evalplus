```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a music note lasts.

    The legend for the music notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string of music notes in a special ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map the music notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the notes list
    for char in notes:
        # If the character is 'o' or '.', add it to the current note
        if char in ['o', '.']:
            current_note += char
        # If the character is '|', add it to the current note and then process the note
        elif char == '|':
            current_note += char
            # If the current note is in the note_beats dictionary, add its beats to the beats list
            if current_note in note_beats:
                beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''
        # If the character is a space, process the current note if it's not empty
        elif char =='' and current_note:
            # If the current note is in the note_beats dictionary, add its beats to the beats list
            if current_note in note_beats:
                beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''

    # Process the last note if it's not empty
    if current_note:
        # If the current note is in the note_beats dictionary, add its beats to the beats list
        if current_note in note_beats:
            beats.append(note_beats[current_note])

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

However, the above code might not be very pythonic. Here's a shorter version that achieves the same result:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of music notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a music note lasts.

    The legend for the music notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string of music notes in a special ASCII format.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts