```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.': 1, 'oO': 4, 'oO|': 2, 'OO|': 1
    }
    return [notes[note] for note in music_string.test_music = [
        "ooO|OO|.o|oo|".split()
    for note in test_music: assert parse_music(note) == [4, 2, 1]
```