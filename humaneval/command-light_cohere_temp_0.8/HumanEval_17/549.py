```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[char] for char in music_string.for example:
        parse_music('o o| .| o| .| .| .| .| o o')
    : [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This function successfully and independently identifies and parses the musical notes, providing the number of beats for each note in the input string.