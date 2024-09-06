Here is a Python script that demonstrates a self-contained function to solve the problem of parsing and returning the number of beats for each musical note in a given string:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a music string representing notes and return list of beat counts.
    Notes are formatted like "beatname beatnumber beat identifier".

    Beat identifiers are either 'o' for whole note, 'o|' for half note, '.|' for quarter note.

    >>>
    parse_music('o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    """
    def get_beat(beatident: str) -> int:
        """Returns the beat identifier corresponding to the input string."""
        if beatident == 'o':
            return 4
        elif beatident == 'o|':
            return 2
        elif beatident == '|':
            return 1
        else:
            raise ValueError("Invalid beat identifier")

    beat_counts = []
    notes = music_string.split(' ')

    for note in notes:
        beat = get_beat(note)
        beat_counts.append(beat)
    return beat_counts

# Test the function
music_str = "o o| .| o| .| .| .| o o"
beat_counts = parse_music(music_str)
print(beat_counts)
```

This script provides a complete solution to the problem of parsing and returning the number of beats for each musical note in a given string. 

It defines a function called `parse_music` that takes a string of music notes as input and returns a list of integers representing the number of beats for each note. The `parse_music` function uses a nested helper function, `get_beat`, which returns the appropriate beat count for a given note identifier.

The `parse_music` function splits the input string into a list of notes, and then iterates over each note to call the `get_beat` function and append the beat count to a list of beat counts. The function then returns the `beat_counts`, which is a list of beat counts corresponding to each musical note in the string.