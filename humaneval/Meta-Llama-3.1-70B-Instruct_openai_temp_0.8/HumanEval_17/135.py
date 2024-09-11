```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format.
    It returns a list of integers corresponding to how many beats each note lasts.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    
    # Create a dictionary to map notes to their corresponding beats
    note_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Iterate over the notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it's a whole note, check if the next note is also 'o'
            if i + 1 < len(notes) and notes[i + 1] == 'o':
                # If it's 'oo', it's a whole note, add 4 beats
                beats.append(note_beats['o'])
                i += 2
            else:
                # If it's not 'oo', check if the next note is '|'
                if i + 1 < len(notes) and notes[i + 1] == '|':
                    # If it's 'o|', it's a half note, add 2 beats
                    beats.append(note_beats['o|'])
                    i += 2
                else:
                    # If it's not 'o|', it's a whole note, add 4 beats
                    beats.append(note_beats['o'])
                    i += 1
        elif notes[i] == '.':  # Check if the current note is a quarter note
            # If it's a quarter note, it must be '.|', add 1 beat
            beats.append(note_beats['.|'])
            i += 2

    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```