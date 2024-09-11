```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes
    :return: A list of integers representing the number of beats each note lasts
    """

    # Define a dictionary to map the notes to their corresponding beats
    note_to_beats = {
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
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its beats to the list
            if current_note:
                beats.append(note_to_beats[current_note])
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char

    # Add the beats of the last note to the list
    if current_note:
        beats.append(note_to_beats[current_note])

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script first defines a dictionary to map the notes to their corresponding beats. It then iterates over the input string, building up the current note and adding its beats to the list when it encounters a space. Finally, it adds the beats of the last note to the list and returns the list of beats.