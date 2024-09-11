```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses the string, and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Create a dictionary to map the notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note in the notes list
    i = 0
    while i < len(notes):
        # Check if the note is 'o' and the next note is '|'
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If true, append the beats of 'o|' to the beats list and increment the index by 2
            beats.append(note_beats['o|'])
            i += 2
        # Check if the note is 'o'
        elif notes[i] == 'o':
            # If true, append the beats of 'o' to the beats list and increment the index by 1
            beats.append(note_beats['o'])
            i += 1
        # Check if the note is '.|'
        elif notes[i] == '.|':
            # If true, append the beats of '.|' to the beats list and increment the index by 1
            beats.append(note_beats['.|'])
            i += 1

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```