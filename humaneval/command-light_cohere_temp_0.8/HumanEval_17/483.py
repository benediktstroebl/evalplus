```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    
    notes_list = [notes.get(note) for note in music_string.
    
    return [notes_list

# Further test
music_string = "o o| .| o| .| .| .| .| o o"
notes_list = parse_music(music_string)
assert len(notes_list) == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
```