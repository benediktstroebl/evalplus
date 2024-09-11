```python
from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Create a dictionary to map the ASCII notes to their respective beats
    note_beats: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string by space to get individual notes
    notes: List[str] = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats: List[int] = []

    # Iterate over each note
    for note in notes:
        # Check if the note is in the dictionary
        if note in note_beats:
            # If it is, append its beats to the list
            beats.append(note_beats[note])
        else:
            # If it's not, raise a ValueError with a meaningful message
            raise ValueError(f"Invalid note: {note}")

    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```