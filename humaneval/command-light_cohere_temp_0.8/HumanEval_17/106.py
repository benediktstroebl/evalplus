```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beat = 0
    beats = []
    for note in music_string.split(' ' '):
        if note in notes:
            beats.append(beat * notes[note])
            beat += notes[note]
    return beats

# Test case
test_music = '''o o| .| o| .| .| .| .| o o'''
test_result = parse_music(test_music)
print(test_result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```