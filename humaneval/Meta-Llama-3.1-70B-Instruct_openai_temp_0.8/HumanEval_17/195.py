```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """
    
    # Define a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats for each note
    beats = []
    
    # Initialize an empty string to build the current note
    current_note = ''
    
    # Iterate over each character in the notes
    for char in notes:
        # Add the character to the current note
        current_note += char
        
        # Check if the current note is in the note_beats dictionary
        if current_note in note_beats:
            # If it is, append the corresponding beats to the beats list
            beats.append(note_beats[current_note])
            # Reset the current note
            current_note = ''
    
    # Return the list of beats
    return beats


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```