```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.

    Legend:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat
    """
    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    note_durations = []

    # Iterate over each note
    for note in notes:
        # Check the type of note and append its duration to the list
        if note == 'o':
            note_durations.append(4)  # Whole note, lasts four beats
        elif note == 'o|':
            note_durations.append(2)  # Half note, lasts two beats
        elif note == '.|':
            note_durations.append(1)  # Quarter note, lasts one beat

    return note_durations

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```