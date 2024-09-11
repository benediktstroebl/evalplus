```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer corresponds to the number of beats a note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """
    
    # Create a dictionary to map the musical notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the beats of each note
    beats = []
    
    # Initialize an empty string to build a note that spans multiple characters
    current_note = ''
    
    # Iterate over each character in the input string
    for note in notes:
        current_note += note
        
        # If the current note is in the dictionary, add its beats to the list
        if current_note in note_beats:
            beats.append(note_beats[current_note])
            current_note = ''
    
    # Return the list of beats
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines the `parse_music` function as specified, using a dictionary to map the musical notes to their corresponding beats. The function splits the input string into a list of notes and then iterates over each character, building and parsing notes as it goes. The beats of each note are added to a list, which is returned at the end.