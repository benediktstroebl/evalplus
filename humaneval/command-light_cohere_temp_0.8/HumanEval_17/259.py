```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    w|' music_string.split(' ')
    would get the pattern to determine note value and beat length, creating list of beats.
 music_string = "o o| .| o| .| .| .| .| o o"
notes = {'o': 4, 'o|': 2, '.|': 1}
beats = music_string.split(' ') w|' music_string.split(' ')

beats = [beat.beat length of beat is length of notes[beat] within music_string]
beats. values = map(lambda beat: notes[beat], beats)
return beats
```