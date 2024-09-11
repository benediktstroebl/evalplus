```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.
    
    Args:
    music_string (str): A string containing musical notes.
    
    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats
    beats = []
    
    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it's a whole note, append its beats and skip the next character
            beats.append(note_beats['o'])
            i += 2
        # Check if the note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # If it's a half note or a quarter note, append its beats
            beats.append(note_beats[notes[i]])
            i += 1
        else:
            # If it's a whole note, append its beats
            beats.append(note_beats['o'])
            i += 1
    
    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```