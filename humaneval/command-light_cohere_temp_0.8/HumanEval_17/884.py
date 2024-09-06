```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = {note: 4 for note in notes}

    def get_beats(note):
        return beats.get(note)

    return [get_beats(note) for note in music_string.map]
```