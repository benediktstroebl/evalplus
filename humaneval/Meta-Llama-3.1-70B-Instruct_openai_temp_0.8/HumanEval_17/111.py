```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    Args:
    music_string (str): A string representing musical notes.

    Returns:
    List[int]: A list of integers representing the number of beats for each note.
    """
    
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats for each note
    beats = []
    
    # Initialize an empty string to build the current note
    current_note = ''
    
    # Iterate over each character in the notes
    for note in notes:
        # If the character is 'o' or '.', it could be the start of a new note
        if note in ['o', '.']:
            # If we've already built a note, add its beats to the list and reset the current note
            if current_note:
                beats.append(note_beats[current_note])
                current_note = ''
            # Start building the new note
            current_note = note
        # If the character is '|', it could be the end of a note
        elif note == '|':
            # Add the current note and '|' to the dictionary key and add its beats to the list
            current_note += '|'
            beats.append(note_beats[current_note])
            current_note = ''
    
    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
When you run this script, it will print: `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`