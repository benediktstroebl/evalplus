```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats
    beats = []
    
    # Iterate over each note in the list
    for note in notes:
        # Append the beats corresponding to the current note to the list
        beats.append(note_beats.get(note, 0))
    
    # Return the list of beats
    return beats


# Example usage:
parse_music('o o|.| o| o|.|.|.|.| o o')
```
In this script, we first define a dictionary to map each musical note to its corresponding beats. We then split the input string into a list of notes, and iterate over each note. For each note, we append its corresponding beats to a list. Finally, we return this list of beats. If a note is not recognized, we append 0 beats to the list.