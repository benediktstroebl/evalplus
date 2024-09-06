```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o','.'','.','.'.r', 'o', '.', 'o', 'o','.|','', '.','.|', '.']
    beats = {4, 2, 1, 1, 2, 2, 1, 1, 1, 4, 4}
    
    for note in notes:
        beat = beats[note.index(len.index(note)]
        note_count = beat
        for beat_num, beat_count in enumerate(music_string.split('\n ':')):
            if beat == 'o':
                if note_count == 4:
                    beat_count = 4
                elif note_count == 2:
                    beat_count = 2
                elif beat_count == beat_count:
                    break
            elif beat == '.':
                if note_count == 1:
                    beat_count = 1
                elif note_count == 4:
                    beat_count = 4
                elif beat_count == beat_count:
                    break
            elif beat == 'o|':
                if note_count == 2:
                    beat_count = 2
                elif note_count == 4:
                    beat_count = 2
                elif beat_count == beat_second:
                    beat_count = beat_count
                    break
            else:
                raise ValueError("Invalid music string")
                
    return beat_count
```