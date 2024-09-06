```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = [4, 2, 1]
    symbols = {'o': 4, 'o|': 2, '|': 1}
    
    notes = [symbols.get(note) for note in music_string.format(' '.join(notes))
    
    return [beats.get(beats.get(note) for note in notes]
```