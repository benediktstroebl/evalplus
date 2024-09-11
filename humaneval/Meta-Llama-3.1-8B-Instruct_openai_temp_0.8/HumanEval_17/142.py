```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format and returns a list of integers corresponding to the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map notes to their corresponding beat lengths
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the parsed notes
    parsed_notes = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Get the beat length of the current note from the dictionary
        beat_length = note_beats[note]

        # Append the beat length to the parsed notes list
        parsed_notes.append(beat_length)

    # Return the parsed notes list
    return parsed_notes

# Test the function with the provided example
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format as input and returns a list of integers corresponding to the number of beats each note lasts. It uses a dictionary to map notes to their corresponding beat lengths and splits the input string into individual notes to parse them. The function is then tested with the provided example.