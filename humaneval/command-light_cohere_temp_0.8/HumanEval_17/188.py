```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beats = music_string.split(' 'o  )
    for note in notes:
        beats = beats.split('|')
        tobeat = beats.fold(beat + notes[note] * 4 if note == 'o'
        beat = beat[0] + beat[1] if len(beat) > 1 else beat[0]
        return beat

# Test cases
assert parse_music('o o| .| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o o o o o o| .') == [12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
assert parse_music('.|') == [1]
assert parse_music('o|') == [2]
```