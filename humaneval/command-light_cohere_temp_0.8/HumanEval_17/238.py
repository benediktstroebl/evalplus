```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes.get(note) for note in music_string.format = r'\n' 4s' 
```
This function is designed to parse and convert a string of musical notes into a list of integers representing the duration of each note in beats. It uses a simple dictionary to map musical symbols to note durations and then iterates over each note in the input string to populate the list of durations.