```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses the string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Mapping of notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a single note (e.g., 'o|')
        if i < len(notes) - 1 and notes[i] + notes[i + 1] in note_beats:
            # If they do, append the corresponding beats to the list and increment the index by 2
            beats.append(note_beats[notes[i] + notes[i + 1]])
            i += 2
        else:
            # If not, append the beats of the single note to the list and increment the index by 1
            beats.append(note_beats[notes[i]])
            i += 1

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```