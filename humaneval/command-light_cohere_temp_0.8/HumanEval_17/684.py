```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', '.', '|', '.', 'o']
    result = [len(note) for note in notes if note.contains(music_string)]
    return result
```
This Python code defines a function called **parse_music** that takes a string representing a musical score in a specific format and returns a list of the lengths of the notes in the music, based on the given input string.  The input music_string is checked against a list of music notes, and the lengths of the notes are extracted using the **contains** method.