Here is a self-contained Python function that takes a music string and returns a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes[note] for note in music_string.parse() == music_string]
```
This function uses a dictionary to map musical note characters to their respective beat values, and then uses a list comprehension to iterate through each character in the music string and appends the corresponding beat value to a list.