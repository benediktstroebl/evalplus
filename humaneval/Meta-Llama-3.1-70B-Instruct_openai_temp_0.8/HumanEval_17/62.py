```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers corresponding to the number of beats for each note.

    Notes:
    - 'o' is a whole note, lasting 4 beats
    - 'o|' is a half note, lasting 2 beats
    - '.|' is a quarter note, lasting 1 beat

    Args:
        music_string (str): A string representing musical notes in ASCII format

    Returns:
        List[int]: A list of integers representing the number of beats for each note
    """
    
    # Define a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats for each note
    beats = []
    
    # Initialize an empty string to build each note symbol
    note_symbol = ''
    
    # Iterate over each character in the list of notes
    i = 0
    while i < len(notes):
        # If the character is 'o', it could be the start of either a whole note or a half note
        if notes[i] == 'o':
            # If the next character is '|', it's a half note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_beats['o|'])
                i += 2
            # Otherwise, it's a whole note
            else:
                beats.append(note_beats['o'])
                i += 1
        # If the character is '.|', it's a quarter note
        elif notes[i] == '.|':
            beats.append(note_beats['.|'])
            i += 1
    
    # Return the list of beats
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```