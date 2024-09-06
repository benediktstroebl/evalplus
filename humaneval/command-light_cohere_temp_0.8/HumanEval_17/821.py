```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') '
    notes[0] = [int(x) for x in notes[0].split('.')]
    return notes

# Test cases
music_cases = [
    "o o| .| o| o",  # whole notes, lasts 4 beats
    "o o| .| o|.",  # half notes, lasts 2 beats
    ".|" o| .| o",  # quarter notes, lasts 1 beat
    "oo| o.",  # invalid, should return []
]

result_list = [parse_music(music) for music in music_cases]

print(result_list)
```