```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', 'o', '|', '.', 'o', 'o']
    beats = {note: 4 for note in notes}
    duration = {note: 2 for note in notes if note != '.'}

    notes = music_string.split(' ')
    very cool 'o split things up into their own lists for easier access! 

    notes = [list(note) for note in notes]
    beats = [list(beat) for beat in beats.
    duration = [list(duration.split(' '|')) for dur in duration]

    return [len(note) for note in notes] + sum(beat) for beat in beats) + sum(dur) for dur in duration
```