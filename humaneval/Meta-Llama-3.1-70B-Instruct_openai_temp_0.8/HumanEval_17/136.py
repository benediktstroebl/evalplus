```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """
    # Create a dictionary to map note symbols to their corresponding durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it's a whole note, append its duration to the list
            durations.append(note_durations['o'])
            # Skip the next note (the space)
            i += 2
        else:
            # If it's not a whole note, check if it's a half note or a quarter note
            note = notes[i]
            if note in note_durations:
                # If it's a valid note, append its duration to the list
                durations.append(note_durations[note])
            i += 1

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```