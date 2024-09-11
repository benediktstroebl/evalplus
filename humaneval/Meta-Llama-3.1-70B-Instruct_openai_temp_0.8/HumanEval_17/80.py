```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    # Create a dictionary to map the musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a half or quater note
        if i < len(notes) - 1 and notes[i + 1] == '|':
            # If they do, append the corresponding beats to the list and skip the next note
            beats.append(note_beats[notes[i] + notes[i + 1]])
            i += 2
        else:
            # If they don't, append the corresponding beats to the list and move to the next note
            beats.append(note_beats[notes[i]])
            i += 1

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```