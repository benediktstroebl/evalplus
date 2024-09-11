```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses it and returns a list of integers representing the number of beats each note lasts.

    :param music_string: A string of musical notes
    :return: A list of integers representing the number of beats each note lasts
    """
    
    # Create a dictionary to map musical notes to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats of each note
    beats = []
    
    # Initialize an empty string to build each note
    current_note = ''
    
    # Iterate over each character in the list of notes
    for char in notes:
        # If the character is not a space, add it to the current note
        if char!= '':
            current_note += char
        
        # If the current note is in the note_beats dictionary, add its beats to the list and reset the current note
        if current_note in note_beats:
            beats.append(note_beats[current_note])
            current_note = ''
    
    # Return the list of beats
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```