```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses the string, and returns a list of integers corresponding to the 
    number of beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers representing the number of beats for each note
    """
    
    # Create a dictionary to map notes to their respective beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Initialize an empty list to store the beats
    beats = []
    
    # Initialize an empty string to build the current note
    current_note = ''
    
    # Iterate over each character in the music string
    for char in music_string:
        # If the character is a space, it means we've reached the end of a note
        if char =='':
            # If the current note is not empty, add its beats to the list
            if current_note:
                beats.append(note_to_beats[current_note])
                current_note = ''
        else:
            # If the character is not a space, add it to the current note
            current_note += char
    
    # If the music string doesn't end with a space, add the beats of the last note
    if current_note:
        beats.append(note_to_beats[current_note])
    
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```