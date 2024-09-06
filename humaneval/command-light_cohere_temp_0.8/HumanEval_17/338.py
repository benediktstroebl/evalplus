```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    new_beats = []
    for beat in music_string.split(' 'o beat'):
        beat = beat.split(' ')
        new_beats.append(notes[ beat])
        return new_beats
```
This function parses the music_string according to the following rules:
- An `o` represents a whole note, lasting four beats.
- An `o|` represents a half note, lasting two beats.
- A `.|` represents a quarter note, lasting one beat.

The function splits the music_string by space, and then by each beat, and appends the corresponding note to the new_beats list.