```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note
    """

    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quater note
    }

    # Initialize an empty list to store the beats
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its beats to the list
            if current_note:
                beats.append(note_beats[current_note])
                current_note = ''
        else:
            # If the character is not a space, add it to the current note
            current_note += char

    # After iterating over the entire string, add the beats of the last note if it's not empty
    if current_note:
        beats.append(note_beats[current_note])

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```