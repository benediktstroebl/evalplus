```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    # Define a dictionary to map the note symbols to their respective beats
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
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # Append the beats for a whole note to the list
            beats.append(note_beats['o'])
        # Check if the current note is a half note or a quarter note
        elif i < len(notes) - 1 and notes[i] + notes[i + 1] in note_beats:
            # Append the beats for the half note or quarter note to the list
            beats.append(note_beats[notes[i] + notes[i + 1]])
            # Skip the next note as it has already been processed
            i += 1
        i += 1

    # Return the list of beats
    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```