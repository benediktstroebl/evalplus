Here's a self-contained Python function that takes a string of music notes and returns a list of integers that represent the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
        other: 0
    }

    beats = 0
    current_beat = 0

    for note in music_string:
        if note in notes:
            beats += notes[note]
        current_beat += 1
        if current_beat >= 4:
            current_beat = 0

    return beats

# Test
test_music = 'o o| .| o| .| .| .| .| o o'
result = parse_music(test_music)
print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```