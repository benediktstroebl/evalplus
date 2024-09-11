```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map notes to their respective beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the music string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats
    beats = []
    
    # Initialize an empty string to build the current note
    current_note = ''
    
    # Iterate over each character in the notes
    for char in notes:
        # If the character is 'o' or '.|', it's a whole note or a quarter note
        if char in note_beats:
            # If current_note is not empty, it means we've encountered a half note
            if current_note:
                # Add the beats of the half note to the list
                beats.append(note_beats[current_note])
                # Reset current_note
                current_note = ''
            # Add the beats of the whole note or quarter note to the list
            beats.append(note_beats[char])
        else:
            # If the character is '|', it's part of a half note
            # Add the character to current_note
            current_note += char
    
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

Alternatively, you could use regular expressions to achieve the same result:

```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses it and returns a list of integers corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the number of beats each note lasts.
    """
    # Create a dictionary to map notes to their respective beats
    note_beats = {
        'o': 4,
        'o\|': 2,
        '\.\|': 1
    }
    
    # Find all occurrences of notes in the music string
    notes = re.findall('|'.join(note_beats.keys()), music_string)
    
    # Return a list of beats corresponding to the notes
    return [note_beats[note] for note in notes]


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```