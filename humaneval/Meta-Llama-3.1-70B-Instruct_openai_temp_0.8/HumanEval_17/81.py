```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of integers representing the number of beats each note lasts.

    The legend for the musical notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
    """

    # Define a dictionary to map the musical notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note in the list
    i = 0
    while i < len(notes):
        # Check if the current note and the next note form a half note or a quater note
        if i < len(notes) - 1 and notes[i] == 'o' and notes[i+1] == '|':
            # If they do, append the beats for a half note and skip the next note
            beats.append(note_beats['o|'])
            i += 2
        elif i < len(notes) - 1 and notes[i] == '.' and notes[i+1] == '|':
            # If they do, append the beats for a quater note and skip the next note
            beats.append(note_beats['.|'])
            i += 2
        else:
            # If they don't, append the beats for a whole note
            beats.append(note_beats['o'])
            i += 1

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```