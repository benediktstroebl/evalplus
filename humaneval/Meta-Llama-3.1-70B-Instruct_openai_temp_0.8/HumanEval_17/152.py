```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a music string and return a list of integers corresponding to the duration of each note.

    The music string is composed of the following notes:
    - 'o' : whole note, lasts 4 beats
    - 'o|' : half note, lasts 2 beats
    - '.|' : quarter note, lasts 1 beat

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to the duration of each note.
    """
    # Define a dictionary to map the notes to their respective durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the durations of the notes
    note_durations_list = []

    # Iterate over the notes and append their durations to the list
    for note in notes:
        if note == 'o':
            note_durations_list.append(note_durations['o'])
        elif '|' in note:
            note_durations_list.append(note_durations[note])

    # Return the list of note durations
    return note_durations_list


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```