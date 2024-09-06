Here is a self-contained Python function that solves the markdown code block's problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }

    beats = []
    current_beat = 0
    for note in music_string:
        if note in notes: beats.append(current_beat)
        current_beat += notes[note]
        if current_beat >= 4: current_beat = 0

    return beats
```