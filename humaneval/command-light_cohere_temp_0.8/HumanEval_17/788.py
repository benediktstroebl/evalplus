```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = []
    current_beat = 0
    
    for symbol in music_string:
        if symbol in notes:
            beats.append(current_beat)
        current_beat += notes[symbol]
        if symbol == '|':
            current_beat = 0
    
    return beats

# Test
music_str = 'o o| .| o| .| .| .| .| o o'
expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4]
beats = parse_music(music_str)
print(beats)
```