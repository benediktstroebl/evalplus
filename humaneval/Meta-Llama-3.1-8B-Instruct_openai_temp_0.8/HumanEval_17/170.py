```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return list of integers 
    corresponding to how many beats each note lasts.

    The ASCII format is as follows:
    - 'o' - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to how many beats each note lasts
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    note_list = music_string.split()
    
    # Use a list comprehension to create a list of note durations
    beat_list = [notes[note] for note in note_list]
    
    return beat_list

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input and returns a list of integers corresponding to the duration of each note. It uses a dictionary to map the note characters to their respective durations, and then splits the input string into individual notes using the `split` method. The list comprehension `[notes[note] for note in note_list]` is then used to create a list of note durations, which is returned by the function. The script also includes a test case to demonstrate the function's behavior.