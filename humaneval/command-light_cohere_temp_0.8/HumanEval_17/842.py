```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', 'o', '.', '.']
    notes = [note for note in notes if note in music_string]
    
    # Verify that a valid format was passed
    assert len(notes) == 1, "Input string should contain only one note"
    
    note_length = len(notes[0])
    
    # Parse the notes
    beat_count = [4, 2, 1, 2, 1, 1, 1, 4]
    
    # Convert note length to beats
    beats = [note_length // 4 for note_length in notes[0]] + [4]
    
    return beats
```