```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')')
    each_note = []
    for note in notes:
        #split to remove 'o|' and '.' characters
        note = note.split('|')
        notes.split(' ')')
        whole_note = int(note[0])
        half_note = int(note[1])
        quarter_note = int(note[2])
        each_note.append(whole_note)
        each_note.append(half_note)
        each_note.append(quarter_note)
    return each_note
```
The function splits the music string into individual notes, then further splits each note into the beat length (whole, half, or quarter) and stores the beat length for each note in the resulting list.