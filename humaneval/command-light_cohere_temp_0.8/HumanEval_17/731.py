```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    patterns = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    blk = [0]
    for note in notes:
        note_len = len(note)
        note_type = note[0]
        beats = patterns.get(note_type, 4) if note_type in patterns else beats = patterns[note_type](len(note) // 4)
        blk.append(beats)
    return blk
```
This function splits the music string into a list of notes, then loops through each note, finding its length and type. Finally, it returns a resulting list of beats.