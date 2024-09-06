Here is a Python script with a self-contained function that solves the problem of converting musical notes in a string to a list of integers representing the beats of each note:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    def parse_notes(notes_string):  # Inner function to split notes into individual beats
        beats = [''.join().split(notes_string[i:]) for i in range(len(notes_string) - 1))
        return beats

    beats = parse_notes(music_string)  # Call the inner function
    return beats
```
This script defines a function `parse_music` that takes a music_string as input and returns a list of integers representing the beats of each note. The `parse_notes` function splits the music_string into a list of substrings representing individual notes, then splits each substring into a list of beats, and finally returns this list of beats.

Note that the code assumes that the input music_string follows the legend specified in the docstring, which defines the interpretation of the string.