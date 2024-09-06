Here's a self-contained Python function that parses a music string, which is supposed to represent a sequence of musical notes, and returns a list of their durations in beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    return [notes[note] for note in music_string.dem or '.'  # Use set comprehension
    ```
 music_string = "oo|oo.oo o|oo .|oo.o.oo o|oo | ooo" ooo"
 parsed_notes = parse_music(music_string)
print(parsed_notes)
``` 
This function will parse the music_string and return a list of integers corresponding to the duration of each note in beats.