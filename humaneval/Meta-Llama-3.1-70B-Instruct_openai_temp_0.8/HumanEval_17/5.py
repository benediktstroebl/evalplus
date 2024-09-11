```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format, 
    and returns a list of integers corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Create a dictionary to map musical notes to their corresponding beats
    note_beats = {
        'o': 4, 
        'o|': 2, 
        '.|': 1
    }
    
    # Split the music string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats of each note
    beats = []
    
    # Initialize an empty string to build each note
    note = ''
    
    # Iterate over each character in the notes
    for char in notes:
        # Add the character to the note
        note += char
        
        # If the note is in the note_beats dictionary, add its beats to the beats list
        if note in note_beats:
            beats.append(note_beats[note])
            # Reset the note
            note = ''
    
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```