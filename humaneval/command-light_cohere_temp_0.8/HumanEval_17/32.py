```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split(' ')
    Music to integer beats list.

notes = [beats.length for beats_list in beats.split('\n') for beat in beats_list for beat in beats]

return notes.length for note in notes:
note_ = notes[note]
print(note_ * beats)
```