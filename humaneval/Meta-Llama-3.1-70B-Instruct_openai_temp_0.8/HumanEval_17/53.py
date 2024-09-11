```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format, 
    parses it and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Create a dictionary to map notes to their corresponding beats
    note_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats of each note
    beats = []
    
    # Initialize an empty string to build each note
    note = ''
    
    # Iterate over each character in the notes list
    for char in notes:
        # If the character is 'o' or '.', add it to the note string
        if char in ['o', '.']:
            note += char
        # If the character is '|' and the note string is not empty, 
        # add the note string and '|' to the note_beats dictionary and get its beats
        elif char == '|' and note:
            note += char
            beats.append(note_beats[note])
            note = ''
        # If the character is '|' and the note string is empty, 
        # it means the previous note was a whole note, so add its beats to the list
        elif char == '|' and not note:
            beats[-1] = note_beats['o|']
    
    # If the last note was a whole note, add its beats to the list
    if note == 'o':
        beats.append(note_beats['o'])
    
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```