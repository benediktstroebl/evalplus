```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' ')
    ...['o', 'o|', '|', '.']
    return [int(beat) for beat in beats.make(Map(notes))]
```
This Python function, parse_music, is designed to parse and transform music notes into a list of integers. It does this by using the Map data structure to transform the string into numbers that represent the duration of each note. The code is self-contained, and it can be used to solve the problem of parsing music notes into beats.