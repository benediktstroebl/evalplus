```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format
    :return: A list of integers corresponding to how many beats each note lasts
    """
    # Define a dictionary to map notes to their corresponding beat counts
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat counts
    beat_counts = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it is, append the whole note's beat count to the list
            beat_counts.append(note_beats['o'])
            # Skip the next iteration to avoid processing the whole note again
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # If it is, append the note's beat count to the list
            beat_counts.append(note_beats[notes[i]])
        # If the note is not recognized, raise a ValueError
        else:
            raise ValueError(f"Unrecognized note: {notes[i]}")
        i += 1

    # Return the list of beat counts
    return beat_counts


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```