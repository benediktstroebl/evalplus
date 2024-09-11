```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses it and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string of musical notes.

    Returns:
        List[int]: A list of integers representing the duration of each note in beats.
    """
    
    # Define a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the durations of the notes
    durations = []
    
    # Initialize an empty string to build each note
    note = ''
    
    # Iterate over each character in the list of notes
    for char in notes:
        # If the character is 'o', add it to the note
        if char == 'o':
            note = char
        # If the character is '|' or '.', add it to the note and get its duration
        elif char in ['|', '.']:
            note += char
            # Get the duration of the note and add it to the list of durations
            durations.append(note_durations[note])
            # Reset the note
            note = ''
        # If the character is a space, do nothing
    
    # Return the list of durations
    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```