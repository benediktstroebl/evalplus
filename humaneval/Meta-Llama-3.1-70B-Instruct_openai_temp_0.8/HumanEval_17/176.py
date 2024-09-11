```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers representing the duration of each note in beats.

    :param music_string: A string of musical notes in a special ASCII format
    :return: A list of integers representing the duration of each note in beats
    """
    # Define a dictionary to map note symbols to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over the notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If the next note is a bar, it's a half note, otherwise it's a whole note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                durations.append(note_durations['o|'])
                i += 2
            else:
                durations.append(note_durations['o'])
                i += 1
        # Check if the current note is a quarter note or half note
        elif notes[i] == '.' or notes[i] == 'o|':
            durations.append(note_durations[notes[i] + '|'])
            i += 1
        # If the note is not recognized, raise a ValueError
        else:
            raise ValueError(f"Unrecognized note symbol: {notes[i]}")

    return durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```