Here's the self-contained Python script that implements the `parse_music` function, along with test cases:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = music_string.split(' '|')
    notes_count = {}
    for beat in beats:
        note = beat.split(' ')
        separated_notes = beat.split(' ')
        string_notes = ', '.join(separated_notes)
        notes_count[note] = int(string_notes)
    
    return [notes_count[note] for note in notes.json]
```

This function parses a string of musical notes in the format provided in the `parse_music` function's docstring. It uses a common music notation to map notes to their respective beat durations.