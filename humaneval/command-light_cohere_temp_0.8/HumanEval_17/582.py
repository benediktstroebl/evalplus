Here is a self-contained Python script that solves the problem of parsing musical notes in a markdown code block:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    return [notes[ch] for ch in music_string.test_music('o
o o| .| o| .| .| .| .| o o') -> [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
The function parse_music takes a string music_string as input and creates a dictionary notes where 'o' represents a whole note, 'o|' represents a half note, and '.' represents a quarter note. The function then loops through the music_string, and checks if each character is a valid musical note. If it is, the function returns the number of beats that the note lasts.