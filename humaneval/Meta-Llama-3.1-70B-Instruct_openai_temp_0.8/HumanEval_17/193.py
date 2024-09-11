```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    and returns a list of integers corresponding to the duration of each note in beats.

    The legend for note durations is as follows:
    - 'o' : whole note, lasts 4 beats
    - 'o|' : half note, lasts 2 beats
    - '.|' : quarter note, lasts 1 beat
    """

    # Create a dictionary to map note symbols to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the input string
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it's a whole note, add its duration to the list
            durations.append(note_durations['o'])
            # Skip the next note (it's part of the whole note)
            i += 2
        elif notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it's a half note, add its duration to the list
            durations.append(note_durations['o|'])
            # Skip the next note (it's part of the half note)
            i += 2
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it's a quarter note, add its duration to the list
            durations.append(note_durations['.|'])
            # Skip the next note (it's part of the quarter note)
            i += 2
        else:
            # If it's just an 'o' or '.' without a following '|' or'', raise a ValueError
            raise ValueError(f"Invalid note symbol: {notes[i]}")

    # Return the list of note durations
    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```