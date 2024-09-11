```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Define a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats for each note
    beats = []
    
    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it's a half note, append its beats to the list and move to the next note
            beats.append(note_beats['o|'])
            i += 2
        elif notes[i] == 'o':
            # If it's a whole note, append its beats to the list and move to the next note
            beats.append(note_beats['o'])
            i += 1
        elif notes[i] == '.|':
            # If it's a quarter note, append its beats to the list and move to the next note
            beats.append(note_beats['.|'])
            i += 1
        else:
            # If the note is not recognized, raise a ValueError
            raise ValueError(f"Unrecognized note: {notes[i]}")
    
    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```