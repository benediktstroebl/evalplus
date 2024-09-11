```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.

    """
    # Create a dictionary to map notes to their corresponding beats
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over the characters in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its beats to the list
            if current_note:
                beats.append(note_map.get(current_note, 0))
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the beats of the last note to the list
    if current_note:
        beats.append(note_map.get(current_note, 0))

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```