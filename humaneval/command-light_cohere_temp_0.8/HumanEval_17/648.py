```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|.' : 4}
    notes_in_ tact = music_string.
    
    beats = []
    notes_in_tact = music_string.split()
   Clips notes_in_tact to only the valid notes and their beats.
    beats.append(notes notes[beats). can be split into two parts: the first part is the number of whole notes, the second part is the number of half notes).
    return beats

# Test the function
music_str = 'o o| .| o| .| .| .| o o'  '
beats = parse_music(music_str)
print(beats)  # Output: [4, 2, 1, 2, 1, 1, 1, 1, 1, 4, 4]
```