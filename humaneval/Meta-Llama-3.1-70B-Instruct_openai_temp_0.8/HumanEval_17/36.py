```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats each note lasts.

    :param music_string: A string of musical notes in a special ASCII format
    :return: A list of integers representing the number of beats each note lasts
    """
    # Split the input string into a list of notes
    notes = music_string.split()

    # Create a dictionary to map each note to its corresponding number of beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the number of beats for each note
    beats = []

    # Iterate over each note in the list of notes
    for note in notes:
        # Check if the note is in the dictionary
        if note in note_to_beats:
            # If the note is in the dictionary, append its corresponding number of beats to the list
            beats.append(note_to_beats[note])
        else:
            # If the note is not in the dictionary, raise a ValueError
            raise ValueError(f"Invalid note: {note}")

    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```