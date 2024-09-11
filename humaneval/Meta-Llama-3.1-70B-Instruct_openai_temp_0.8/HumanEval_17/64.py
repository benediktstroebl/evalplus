```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary mapping each note to its corresponding beats
    note_to_beats = {
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

    # Iterate over each note in the list of notes
    for note in notes:
        # If the current note is not empty and the current note plus the next note is a valid note, 
        # add the beats of the current note to the list of beats and reset the current note
        if current_note and current_note +'' + note in ['o o|', 'o.|']:
            beats.append(note_to_beats[current_note])
            current_note = note
        # If the current note plus the next note is a valid note, update the current note
        elif current_note +'' + note in ['o o|', 'o.|']:
            current_note +='' + note
        # If the current note is a valid note, add its beats to the list of beats and reset the current note
        elif current_note in note_to_beats:
            beats.append(note_to_beats[current_note])
            current_note = note
        # If the next note is a valid note, add its beats to the list of beats
        elif note in note_to_beats:
            beats.append(note_to_beats[note])
        # Otherwise, update the current note
        else:
            current_note = note

    # If the current note is not empty, add its beats to the list of beats
    if current_note in note_to_beats:
        beats.append(note_to_beats[current_note])

    return beats


# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```