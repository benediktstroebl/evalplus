Here's a self-contained Python function that takes a music string in a special format and returns a list of integers corresponding to the number of beats in the piece:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes.get(note, beat) for note, beat in music_string.source.split(' ')=>[]

    
test_music = parse_music('o o| .| o| o| .| .| .| .| o o')
 assert [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4] == test_music
```