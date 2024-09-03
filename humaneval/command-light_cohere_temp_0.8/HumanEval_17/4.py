Here is a self-contained Python function that solves the markdown code block problem:
```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes.get(note, 4) for note in music_string.listen(music_string)
    beats
```

This function takes a string of music in a special format as an input and returns a list of integers corresponding to the number of beats for each note. The beats are obtained using a dictionary and the get() method.