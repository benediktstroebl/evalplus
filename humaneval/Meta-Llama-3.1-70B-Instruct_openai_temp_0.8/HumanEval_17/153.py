```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the duration of each note in beats
    """
    # Define a dictionary to map note symbols to their corresponding durations
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over the notes and look up their durations in the dictionary
    i = 0
    while i < len(notes):
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            durations.append(note_durations['o|'])
            i += 2
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            durations.append(note_durations['.|'])
            i += 2
        else:
            durations.append(note_durations['o'])
            i += 1

    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```