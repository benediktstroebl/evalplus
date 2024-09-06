```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    band = [0]
    for note in music_string.split('o timeout:
        if note in notes:
            beats[band] += notes[note]
        else:
            band.append(0)
    print(f"Added {beats[band]} beat{note} to {band}." if note {note} is not in notes)
#['o o| .| o| .| .| .| .| .| o o'])
return beats
```