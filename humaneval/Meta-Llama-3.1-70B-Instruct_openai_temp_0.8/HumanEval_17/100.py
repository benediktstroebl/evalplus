```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """

    # Create a dictionary to map the note representations to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the list of notes
    for char in notes:
        # If the character is 'o' or '.', it's the start of a new note, so add the current note to the list
        # of beats and reset the current note
        if char in ['o', '.']:
            if current_note in note_beats:
                beats.append(note_beats[current_note])
            current_note = char
        # If the character is '|' and the current note is not empty, add the current note to the list of
        # beats and reset the current note
        elif char == '|' and current_note:
            current_note += char
            beats.append(note_beats[current_note])
            current_note = ''
        # If the character is'', it's the end of a note, so add the current note to the list of beats and
        # reset the current note
        elif char == '':
            if current_note in note_beats:
                beats.append(note_beats[current_note])
            current_note = ''

    # Add the last note to the list of beats if it's not empty
    if current_note in note_beats:
        beats.append(note_beats[current_note])

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```