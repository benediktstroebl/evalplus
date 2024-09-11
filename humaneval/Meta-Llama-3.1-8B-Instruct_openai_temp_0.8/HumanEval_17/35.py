### Musical Note Parser
#### A Python Script to Parse Musical Notes from a String

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return a list of integers corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    
    # Define a dictionary to map note types to their corresponding beat durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}
    
    # Initialize an empty list to store the note durations
    beat_durations = []
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Iterate over each note in the list
    for note in notes:
        # Append the duration of the current note to the beat_durations list
        beat_durations.append(note_durations[note])
    
    # Return the list of beat durations
    return beat_durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this script, the `parse_music` function takes a string representing musical notes in ASCII format as input and returns a list of integers corresponding to the number of beats each note lasts. The function uses a dictionary to map note types to their corresponding beat durations and then iterates over each note in the input string to calculate the duration of each note. The example usage at the end demonstrates how to use the function to parse a string of musical notes.