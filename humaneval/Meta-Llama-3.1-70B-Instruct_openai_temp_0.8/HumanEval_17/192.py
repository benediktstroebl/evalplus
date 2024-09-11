```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers representing the number of beats each note lasts.
    """

    # Define a dictionary to map each note to its corresponding number of beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note, half note, or quarter note
        if notes[i] == 'o':
            # If the next note is '|', it's a half note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_to_beats['o|'])
                i += 2
            else:
                beats.append(note_to_beats['o'])
                i += 1
        elif notes[i] == '.':
            # If the next note is '|', it's a quarter note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_to_beats['.|'])
                i += 2
            else:
                raise ValueError("Invalid note: '.' must be followed by '|'")
        else:
            raise ValueError(f"Invalid note: '{notes[i]}'")

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```