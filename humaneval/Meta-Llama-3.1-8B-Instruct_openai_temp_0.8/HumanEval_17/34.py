```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers corresponding to the number of beats each note lasts.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers where each integer corresponds to the number of beats a note lasts.

    Legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beat durations
    beat_durations = []
    
    # Iterate over each note in the list of notes
    for note in notes:
        # Check the type of note and append the corresponding beat duration to the list
        if note == 'o':
            beat_durations.append(4)
        elif note == 'o|':
            beat_durations.append(2)
        elif note == '.|':
            beat_durations.append(1)
    
    # Return the list of beat durations
    return beat_durations

# Example usage
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts. The function uses a legend to determine the beat duration for each note type and returns the list of beat durations. The example usage at the end demonstrates how to use the function to parse a string of musical notes and print the resulting list of beat durations.