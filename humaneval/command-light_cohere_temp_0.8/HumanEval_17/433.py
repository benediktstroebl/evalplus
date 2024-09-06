```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = {note: 4 for note in notes}  # whole note lasts 4 beats
    half_beats = beats. 'o half note lasts 2 beats
    notes += ['o|']
    quarter_beats = beats. '.|' lasts 1 beat
    add notes += ['|']
    return [beats[note] for note in notes]

# test the function
print(parse_music('o o| .| o| .| .| .| .| o o'))
 ```