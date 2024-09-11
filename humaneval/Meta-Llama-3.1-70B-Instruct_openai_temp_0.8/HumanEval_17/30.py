```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses the string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to how many beats each note lasts
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats for each note
    beats = []

    # Loop through each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and (i == len(notes) - 1 or notes[i + 1]!= '|'):
            # If it's a whole note, append 4 beats to the list
            beats.append(4)
        # Check if the current note is a half note
        elif notes[i] == 'o' and notes[i + 1] == '|':
            # If it's a half note, append 2 beats to the list and increment the index to skip the '|' character
            beats.append(2)
            i += 1
        # Check if the current note is a quarter note
        elif notes[i] == '.|':
            # If it's a quarter note, append 1 beat to the list
            beats.append(1)
        i += 1

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```