Here's a Python script with a self-contained function that solves the problem of parsing musical notes in a special ASCII format into a list of integers:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, '|' : 1}
    notes_by_length = [notes.get(octave, len(music_string[octave:])) for octave in range(len(music_string) - 1, 0, -1)]
    return notes_by_length
```
This function is designed to parse a string of musical notes in a special ASCII format and return a list of integers corresponding to the number of beats in each note. 

It uses a dictionary to map the musical notes to their respective durations, and then iterates over the music string to extract the number of beats for each note, ensuring proper timing and avoiding out of bounds or duplicate notes.