```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a note lasts.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """

    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats of the notes
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the music string
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

    # Add the beats of the last note to the list
    if current_note:
        beats.append(note_beats[current_note])

    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o')) 
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```