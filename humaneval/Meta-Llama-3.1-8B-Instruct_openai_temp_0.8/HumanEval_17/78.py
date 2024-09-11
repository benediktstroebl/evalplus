```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    corresponding to the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in the format described below.

    Returns:
    List[int]: A list of integers where each integer corresponds to the number of beats a note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    
    # Create a dictionary to map the note symbols to their corresponding beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the music string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations
    beat_durations = []

    # Iterate over each note in the notes list
    for note in notes:
        # Append the beat duration for the current note to the beat_durations list
        beat_durations.append(note_durations[note])

    # Return the list of beat durations
    return beat_durations

# Test the function
print(parse_music('o o|.| o| o|.|..|..|. o o'))
```

This script first defines a dictionary `note_durations` to map the note symbols to their corresponding beat durations. It then splits the input string into individual notes, iterates over each note, and appends the corresponding beat duration to the `beat_durations` list. Finally, it returns the `beat_durations` list. The test at the end demonstrates how to use the `parse_music` function.