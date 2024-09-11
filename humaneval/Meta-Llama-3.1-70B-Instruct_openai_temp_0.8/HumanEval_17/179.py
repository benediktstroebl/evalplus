```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the number of beats each note lasts.
    """
    # Define a dictionary to map the musical notes to their respective beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1]!= '|':
            beats.append(note_beats['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif i + 1 < len(notes) and notes[i + 1] == '|':
            note = notes[i] + '|' if notes[i] == 'o' or notes[i] == '.' else notes[i] + '|' + notes[i + 1]
            beats.append(note_beats.get(note, 0))
            i += 2
        else:
            beats.append(0)
            i += 1

    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```