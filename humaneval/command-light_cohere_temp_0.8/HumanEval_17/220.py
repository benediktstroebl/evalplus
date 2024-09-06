Here's a self-contained Python function that takes a music string in a special format and returns a list of integers that represent how many beats each note lasts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[note] for note in music_string.split(' '|')]
    return beats
```
This function parses the music string and returns a list of integers, which represents how many beats each note lasts. It uses a unique key: note style for its mapping table. The function can be easily reused to solve the same problem with different input music strings.