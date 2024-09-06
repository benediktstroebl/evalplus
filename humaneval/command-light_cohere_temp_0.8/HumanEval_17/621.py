```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beats = music_string.split()
    dry_beat = next(beats)
    notes_dry = [notes[c] for c in dry_beat.split(' '|')]
   
    wet_beat = next(beats)
    wet_notes = [notes[c] for c in wet_beat.split(' '|')]
   
    return wet_notes + [0] + notes_dry
```