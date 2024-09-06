```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_by_length = {len(note): note for note in notes.
    notes = list(notes_by_length.items())
    winner: len(notes), return notes
```