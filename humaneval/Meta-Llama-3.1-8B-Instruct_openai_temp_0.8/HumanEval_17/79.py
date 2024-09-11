### Music Note Parser
#### Python Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Rules:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """
    note_durations = {'o': 4, 'o|': 2, '.|': 1}  # Define note durations
    beats = []  # Initialize an empty list to store note durations

    music_string += '|'  # Add a dummy '|' at the end to handle the last note

    i = 0
    while i < len(music_string):
        note = music_string[i:i+2]  # Extract a note from the string
        beats.append(note_durations[note])  # Append the note's duration to the list
        i += 2  # Move to the next note

    return beats[:-1]  # Return all notes except the dummy '|' at the end

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the duration of each note in beats. It uses a dictionary to map note types to their durations and iterates over the input string to extract note durations. The dummy '|' at the end ensures that the last note is handled correctly. The function is then tested with the provided example.