### Music Parser Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Initialize an empty list to store the results
    beats = []
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Iterate over each note
    for note in notes:
        # Append the beat value of the note to the result list
        beats.append(note_beats.get(note, 0))
    
    # Return the list of beat values
    return beats

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```