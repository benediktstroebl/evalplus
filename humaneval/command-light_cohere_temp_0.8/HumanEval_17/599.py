```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    expected = [notes[i] for i in range(len(beats)) if i in notes.
    return [map(notes.get, beats)]
```
This function parses a string of musical notes, represented in a special ASCII format, and returns a list of integers corresponding to how many beats does each note last. The function utilizes a dictionary `notes` to map the musical notes to the number of beats each one lasts.