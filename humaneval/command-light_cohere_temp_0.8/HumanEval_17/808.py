```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split('|')
    note_lengths = [beats.split('o inside notes]
   
    for note, beat in zip(notes.split('o):
        note = int(note))
        if note in notes:
            note_lengths.append(note * beats.append(note * beats)
        else:
            note_lengths.append(beats)
    return note_lengths
```