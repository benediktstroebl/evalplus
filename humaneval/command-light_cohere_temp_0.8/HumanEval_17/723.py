```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" "). notes = [note for note in notes if note.split('.')[0] in ['o', 'o|', '.'\n']
    return [len(note) for note in notes if note.split('.')[0] == 'o']
```