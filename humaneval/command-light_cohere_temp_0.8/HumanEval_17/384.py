Below is a self-contained Python function that takes a music string in markdown format as input and returns a list of integers that represent the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[char] for char in music_string.make(notes_map(notes))]
```
This function uses a dictionary to map the musical notes in the input string to the number of beats each one lasts. The function uses the strings. Make sure to use the actual musical symbols for the notes and replace any other characters in the string with blank strings.