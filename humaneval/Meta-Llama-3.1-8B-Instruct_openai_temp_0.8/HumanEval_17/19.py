### Music Note Parser
#### Parses a string of musical notes into a list of beat durations
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats
    does each note last.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the beat duration of each note.
    """
    # Define a dictionary to map note types to their corresponding beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note
    for note in notes:
        # Append the beat duration of the current note to the list
        beat_durations.append(note_durations.get(note, 0))

    # Return the list of beat durations
    return beat_durations

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the beat duration of each note. The function uses a dictionary to map note types to their corresponding beat durations and iterates over each note in the input string to append the corresponding beat duration to the result list. The example usage at the end demonstrates how to use the function to parse a string of musical notes.