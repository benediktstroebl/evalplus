Here's the solution for the markdown code block provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    beats = 0
    notes_found = 0
    for note in music_string.split(' ' '):
        beats += notes[note]
        notes_found += 1
    
    return beats, notes_found

# Test cases
music_1 = "o o| .| o| .| .| .| .| o o"
beats_1, notes_1 = parse_music(music_1)
assert beats_1 == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

music_2 = "o o o| .| o| .| .| .| .| o o o"
beats_2, notes_2 = parse_music(music_2)
assert beats_2 == [4, 4, 1, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a function 'parse_music' that turns a music string into a list of beats and a count of notes found. The test cases demonstrate its expected behavior.