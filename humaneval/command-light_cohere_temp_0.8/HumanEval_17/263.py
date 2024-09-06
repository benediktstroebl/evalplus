```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes.get(note) for note in music_string.from(notes)
```

This Python script defines a function named `parse_music` that takes a music string as input and returns a list of integers. It utilizes a legend where 'o' represents a whole note, 'o|' represents a half note, and '.|' represents a quarter note. The function uses a list comprehension and a built-in function `get` to extract these values from the input string.