```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the duration of each note.
    """
    music_dict = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary mapping note types to beats
    beats = []  # Initialize an empty list to store the beats

    music_string += '|'  # Add a '|' at the end to handle trailing notes correctly
    note = ''  # Initialize an empty string to store the current note

    for char in music_string:  # Iterate over each character in the music string
        if char in music_dict:  # If the character is a valid note type
            note += char  # Add the character to the current note
        elif note:  # If the character is not a valid note type and the current note is not empty
            beats.append(music_dict[note])  # Add the duration of the current note to the beats list
            note = ''  # Reset the current note

    return beats[:-1]  # Return the list of beats (excluding the trailing '|' added earlier)

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the duration of each note. The function uses a dictionary to map note types to their respective durations and iterates over the input string to extract the notes and their durations. The function returns the list of beats, excluding the trailing '|' added earlier. The script also includes a test case to verify the function's correctness.