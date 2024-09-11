```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it and returns a list of integers corresponding to the number of beats each note lasts.

    :param music_string: A string of musical notes.
    :return: A list of integers representing the number of beats for each note.
    """
    
    # Define a dictionary to map each note to its corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats for each note
    beats = []
    
    # Initialize an index to keep track of the current position in the notes list
    i = 0
    
    # Loop through the notes list
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If the next note is '|', it's a half note, so add it to the beats list
            if i + 1 < len(notes) and notes[i + 1] == '|':
                beats.append(note_beats['o|'])
                # Skip the '|' note
                i += 2
            else:
                # If it's not a half note, it's a whole note, so add it to the beats list
                beats.append(note_beats['o'])
                i += 1
        # If the current note is a quarter note, add it to the beats list
        elif notes[i] == '.|':
            beats.append(note_beats['.|'])
            i += 1
        # If the current note is a '|' and the previous note is not 'o', it's a quarter note
        elif notes[i] == '|' and (i == 0 or notes[i - 1]!= 'o'):
            beats.append(note_beats['.|'])
            i += 1
        # If none of the above conditions are met, skip the current note
        else:
            i += 1
    
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```