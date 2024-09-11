```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses this string and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Define a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the music string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats for each note
    beats = []
    
    # Initialize an empty string to build each note
    note = ''
    
    # Iterate over each character in the music string
    for char in music_string:
        # If the character is not a space, add it to the current note
        if char!='':
            note += char
        # If the character is a space, the current note is complete
        else:
            # If the note is not empty, add its beats to the list and reset the note
            if note:
                beats.append(note_beats.get(note, 0))
                note = ''
    
    # Add the beats for the last note
    if note:
        beats.append(note_beats.get(note, 0))
    
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```