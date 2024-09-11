```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    legend = {
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
    
    # Iterate over the notes
    for note in notes:
        # If the note contains a space, it's a whole note
        if'' in note:
            # Add the beats of the whole note to the list
            beats.append(legend['o'])
        else:
            # Add the note to the current note
            current_note += note
            
            # If the current note is in the legend, add its beats to the list
            if current_note in legend:
                beats.append(legend[current_note])
                # Reset the current note
                current_note = ''
    
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```