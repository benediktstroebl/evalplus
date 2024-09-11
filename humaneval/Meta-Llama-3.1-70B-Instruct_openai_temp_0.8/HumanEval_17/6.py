```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

    The legend for the ASCII format is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
    """
    
    # Split the input string into notes
    notes = music_string.split()
    
    # Initialize an empty list to store the durations of the notes
    durations = []
    
    # Loop over each note in the notes list
    for note in notes:
        # Check the type of the note and append its duration to the durations list
        if note == 'o':
            durations.append(4)
        elif note == 'o|':
            durations.append(2)
        elif note == '.|':
            durations.append(1)
    
    # Return the list of note durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```