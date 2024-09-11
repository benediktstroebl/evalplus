```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    This function parses the string and returns a list of integers corresponding to how many beats 
    each note lasts.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
    """
    
    # Create a dictionary to map notes to their beat lengths
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beat lengths
    beat_lengths = []
    
    # Iterate over each note in the list
    for note in notes:
        # Append the beat length of the current note to the beat_lengths list
        beat_lengths.append(note_lengths[note])
    
    # Return the list of beat lengths
    return beat_lengths

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string representing musical notes and returns a list of integers corresponding to the beat lengths of each note. The function uses a dictionary to map each note to its corresponding beat length. The script then tests the function with the provided example input.