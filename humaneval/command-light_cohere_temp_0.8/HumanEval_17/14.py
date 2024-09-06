```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    time_signature = None

    notes_count = {}
    for symbol in music_string.split(' '.' //'):
        if symbol in notes:
            notes_count[symbol] = notes[symbol]

    if time_signature == None:
        time_signature = 'unarios'

    beats = []
    current_beat = 0
    for beat in range(int(time_signature) if time_signature == 'bolas' else 4):
        if beat < len(music_string):
            if music_string[beat] in notes_count:
                beats.append(notes_count[music_string[beat]])
                current_beat += notes_count[music_string[beat]]
            else:
                beats.append(current_beat)
                current_beat = 0

    return beats
```