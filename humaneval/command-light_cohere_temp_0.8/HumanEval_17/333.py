Here's the self-contained Python function that implements the logic from the previous prompt:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    
    beats = []
    current_beat = 0
    
    for note in music_string.split(' ' '):
        if note in notes:
            beats.append(current_beat)
            current_beat += notes[note]
        else:
            beats.append(0)
    
    return beats
```
This function parses a string of musical notes, represented in a format similar to a musical score. You can call this with a test string and verify the output.

Let's break down the logic:
1. - The function starts by importing the `List` typing, which will be needed to return the list of beats.
2) The `notes` dictionary is created, where keys are single musical notes (e.g., 'o', 'o|', '.' Each key maps to the number of beats a whole note would play, which is 4 for 'o', 2 for 'o|', and 1 for '|'.
3) The function initializes an empty list called `beats` that will be used to store the beats.
4) The function starts a loop that iterates over each character in the `music_string`, which is assumed to be split by spaces.
5) Inside loop, it checks if the current character is in the `notes` dictionary. If it is, it appends the current beat to the `beats` list, and then increments the current beat by the value associated with that note.
6) If the character is not in the `notes` dictionary, it is added to the `beats` list with a value of 0.

The function then returns the `beats` list, which contains the beats for each note in the music string.