```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beat_count = {note: 4 for note in notes}
    
    notes = music_string.split(' ') ')[0].
    beats = [beat_count.get(note, 4) for note in notes]
    
    return [beats]
```