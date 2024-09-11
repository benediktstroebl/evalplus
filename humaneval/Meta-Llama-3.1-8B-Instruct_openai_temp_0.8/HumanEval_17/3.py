```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string representing musical notes in a special ASCII format
    and returns a list of integers corresponding to how many beats each note lasts.

    The legend is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """

    # Define a dictionary to map notes to their corresponding beat durations
    note_beats = {'o': 4, 'o|': 2, '.|': 1}

    # Initialize an empty list to store the beat durations
    beats = []

    # Split the input string into individual notes
    notes = music_string.split()

    # Iterate over each note in the input string
    for note in notes:
        # Append the beat duration of the current note to the list
        beats.append(note_beats[note])

    # Return the list of beat durations
    return beats

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this script, we first define a dictionary `note_beats` to map each note to its corresponding beat duration. We then split the input string into individual notes using the `split` method, and iterate over each note to append its beat duration to the `beats` list. Finally, we return the `beats` list, which contains the beat durations of all notes in the input string. The test case at the end demonstrates the function's usage.