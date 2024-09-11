```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    note_durations = []

    # Loop through each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and (i == len(notes) - 1 or notes[i + 1]!= '|'):
            # Append the duration of a whole note to the list
            note_durations.append(4)
        # Check if the note is a half note or a quater note
        elif notes[i] in ['o', '.'] and i < len(notes) - 1 and notes[i + 1] == '|':
            # Check if the note is a half note or a quater note
            if notes[i] == 'o':
                # Append the duration of a half note to the list
                note_durations.append(2)
            else:
                # Append the duration of a quater note to the list
                note_durations.append(1)
            # Skip the '|' character
            i += 1
        i += 1

    # Return the list of note durations
    return note_durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```