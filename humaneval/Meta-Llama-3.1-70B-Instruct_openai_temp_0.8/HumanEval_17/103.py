```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in special ASCII format and return a list of integers
    corresponding to the number of beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've finished building a note
        if char =='':
            # If the note is not empty, add its beats to the list
            if note:
                beats.append(note_beats.get(note, 0))
                note = ''
        else:
            # If the character is not a space, add it to the note
            note += char

    # Add the beats of the last note to the list
    if note:
        beats.append(note_beats.get(note, 0))

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```