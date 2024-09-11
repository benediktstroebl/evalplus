```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    individual_notes = music_string.split()
    
    # Initialize an empty list to store the beat durations
    beat_durations = []
    
    # Iterate over each note and add its duration to the list
    for note in individual_notes:
        beat_durations.append(notes.get(note, 'Invalid note'))
    
    # Convert the list to integers (in case a note has a duration of 4)
    beat_durations = [int(dur) for dur in beat_durations]
    
    return beat_durations

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, splits it into individual notes, looks up the duration of each note in a dictionary, and returns a list of integers representing the durations of the notes. If an unknown note is encountered, it defaults to an invalid note. The example usage at the end demonstrates how to use this function to parse a string of musical notes and print the resulting durations.