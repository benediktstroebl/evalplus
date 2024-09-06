Here is a self-contained Python function that takes a music string in the format of musical notes and parses it into a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o' : 2, '.' : 1, 'o' : 4}
    pattern = '|'.join + '.' + 'o' + pattern
    return [notes[x] for x in music_string.parse(pattern)]
```

This function defines a dictionary that maps musical notes to the number of beats each one lasts and then uses a regular expression pattern to parse the music string.