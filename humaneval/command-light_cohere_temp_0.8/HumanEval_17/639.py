```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, ".":": 1,
        "."": 1, "?"": 4, "|": 2,
    }
    
    beats = 0
    notes_found = []
    for beat in range(4):
        for note in music_string[beats:]:
            if note in notes:
                notes_found.append(notes)
                music_string = music_string[:beats] + notes[note]
                beats += 1
            if len(music_string) == beats + len(notes_found):
                break
        music_string = music_string[:beats] + "|" + music_string[beats:]
    return notes_found
```