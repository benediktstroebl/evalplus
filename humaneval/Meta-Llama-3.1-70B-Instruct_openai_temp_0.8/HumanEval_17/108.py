```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it, and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the number of beats each note lasts
    """

    # Define a dictionary to map the music notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Iterate over the notes
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a half or quarter note
        if i < len(notes) - 1 and notes[i] == 'o' and notes[i + 1] == '|':
            # If so, append the corresponding beats to the list and skip the next note
            beats.append(note_beats['o|'])
            i += 2
        elif i < len(notes) - 1 and notes[i] == '.' and notes[i + 1] == '|':
            # If so, append the corresponding beats to the list and skip the next note
            beats.append(note_beats['.|'])
            i += 2
        else:
            # If not, append the corresponding beats to the list and move to the next note
            beats.append(note_beats[notes[i]])
            i += 1

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```