Below is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = {
        'o': 4,
        'o|': 2,
        '|.' : 1
    }
    
    music_notes = music_string.split(' ')')
    
    time_signature = music_notes[0].split(' ')
    staff = int(time_signature[1])
    beat = int(time_signature[2])
    notes = [int(note) for note in music_notes[1].split(' ')]

    return [beats[note] for note in notes] * staff
```