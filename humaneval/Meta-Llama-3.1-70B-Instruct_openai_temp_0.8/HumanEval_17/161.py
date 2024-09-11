```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers representing the number of beats each note lasts.
    """
    
    # Define a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats for each note
    beats = []
    
    # Initialize an empty string to build each note
    current_note = ''
    
    # Iterate over each character in the input string
    for char in music_string:
        # Add the character to the current note
        current_note += char
        
        # If the current note is in the note_beats dictionary, add its beats to the list and reset the current note
        if current_note in note_beats:
            beats.append(note_beats[current_note])
            current_note = ''
    
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```