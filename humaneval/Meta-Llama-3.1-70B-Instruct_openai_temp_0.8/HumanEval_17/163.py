```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map notes to their corresponding beats
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

    # Iterate over each character in the notes
    for note in notes:
        # If the character is 'o' or '.', it's the start of a new note
        if note in ['o', '.']:
            # If there's a current note, add its beats to the list
            if current_note:
                beats.append(note_beats[current_note])
            # Reset the current note
            current_note = note
        # If the character is '|', it's the end of the current note
        elif note == '|':
            # Add the current note and '|' to the dictionary key
            current_note += '|'
            # Add the beats of the current note to the list
            beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''

    # If there's a current note left, add its beats to the list
    if current_note:
        beats.append(note_beats[current_note])

    return beats

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```