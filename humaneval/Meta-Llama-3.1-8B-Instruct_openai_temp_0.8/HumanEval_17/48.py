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
    
    # Create a dictionary to map notes to their beat durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}
    
    # Initialize an empty list to store the beat durations
    beat_durations = []
    
    # Split the input string into notes
    notes = music_string.split()
    
    # Iterate over each note in the input string
    for note in notes:
        # Append the duration of the note to the list
        beat_durations.append(note_durations[note])
    
    # Return the list of beat durations
    return beat_durations

# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))
```

In this script, a dictionary `note_durations` is used to map notes to their beat durations. Then, the input string is split into notes and the beat duration of each note is appended to the list `beat_durations`. Finally, the list of beat durations is returned.