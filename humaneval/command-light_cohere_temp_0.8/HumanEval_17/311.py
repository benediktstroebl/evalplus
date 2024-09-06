Below is a self-contained Python function that parses a music string in markdown code format and returns a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    return [notes[note] for note in music_string.parse("".
```

This function takes a string as input, which is expected to represent musical notes in a special ASCII format. The function then creates a dictionary of notes and their durations, and then loops through each character in the string and uses the `parse` method to split into the individual notes. 

This approach allows the function to be self-contained, and it can be used to parse any string of musical notes in markdown code format into a list of integers representing the durations of the notes.