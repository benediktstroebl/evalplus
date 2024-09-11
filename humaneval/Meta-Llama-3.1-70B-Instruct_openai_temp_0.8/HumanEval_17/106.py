```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the beats of each note
    """

    # Create a dictionary to map each note format to its beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note and the next one form a half or quarter note
        if i + 1 < len(notes) and notes[i+1] == '|':
            # If they do, append the beats of the combined note to the list
            beats.append(note_beats[notes[i] + notes[i+1]])
            # Skip the next note as it has been processed
            i += 2
        else:
            # If they don't, append the beats of the current note to the list
            beats.append(note_beats[notes[i]])
            # Move to the next note
            i += 1

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```