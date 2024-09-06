```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')').
    beats = [int(x) for x in beats if x.strip().
    notes.split(' .')
    period_beats = []
    for beat in beats:
        beat_str = beat.split(' ')
        period = int(beat[0])
        for i, note in enumerate(beat[1:], 1):
            note_value = int(notes[note])
            if i == len(beat) - 1:
                period *= 4
            period *= notes[note]
        period_beats.append(period)
    period_beats.return time = int(period_beats)
    return time
```