Here's a self-contained Python function that takes a string representing music notes in a special ASCII format, then returns a list of integers corresponding to how many beats each note lasts. 

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o' : 2, '.' : 1}
    return [notes[char.strip[music_string.find(note)] for note in notes]
```

This function uses a dictionary to map musical notes to their duration in beats. The function uses the string.tract method of the string to find the note, and then uses the `find()` method to get the index of the note in the dictionary.