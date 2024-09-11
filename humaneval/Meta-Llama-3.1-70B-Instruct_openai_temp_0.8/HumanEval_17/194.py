```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format and returns a list of integers
    corresponding to the number of beats each note lasts.

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """

    # Define a dictionary to map each note to its corresponding number of beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Initialize an empty string to build each note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its beats to the list and reset the current note
            if current_note:
                beats.append(note_beats[current_note])
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the beats of the last note to the list
    if current_note:
        beats.append(note_beats[current_note])

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```