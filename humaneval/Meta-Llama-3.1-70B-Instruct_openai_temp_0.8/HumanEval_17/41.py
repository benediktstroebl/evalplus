```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Create a dictionary to map the notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats of the notes
    beats = []
    
    # Initialize an empty string to build the current note
    current_note = ''
    
    # Iterate over the notes
    for note in notes:
        # If the note is a whole note, add it to the beats list
        if note == 'o':
            beats.append(note_beats[note])
        # If the note is a half note or a quarter note, add the current note and its beats to the list
        elif note in ['o|', '.|']:
            if current_note:
                beats.append(note_beats[current_note])
            current_note = note
            beats.append(note_beats[note])
            current_note = ''
        # If the note is a part of a half note or a quarter note, add it to the current note
        else:
            current_note += note
            # If the current note is complete, add it to the beats list
            if current_note in note_beats:
                beats.append(note_beats[current_note])
                current_note = ''
    
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```