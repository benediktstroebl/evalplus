```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.
    
    Args:
    music_string (str): A string containing musical notes in ASCII format.
    
    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Create a dictionary to map the notes to their respective beat values
    note_beats = {
        'o': 4,      # whole note
        'o|': 2,     # half note
        '.|': 1      # quarter note
    }
    
    # Initialize an empty list to store the beat values of the notes
    beats = []
    
    # Initialize an empty string to build each note
    note = ''
    
    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the note is not empty, add its beat value to the list
            if note:
                beats.append(note_beats.get(note, 0))
                note = ''
        else:
            # Add the character to the current note
            note += char
    
    # Add the beat value of the last note (if any) to the list
    if note:
        beats.append(note_beats.get(note, 0))
    
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```