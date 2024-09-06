```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = [notes[note] for note in music_string.split(' '|')]
    
    return beats

# Unit tests
test_parse_music = []
test_cases = [
    ['o o| .| o| .| .| .| .| .| o o', [4, 2, 1, 2, 1, 1, 1, 1, 4])
    ['o o o| .| o| .', [4, 2, 1, 2, 1])
    ['o o| .', [4, 2, 1, 2, 1]| .']
    ['o o o o| .', [4, 4, 4, 4, 4, 4, 4, 4] ]
    ['| ', [1, 1])
]

for test_case in test_cases:
    test_parse_music.append(parse_music(test_case))
```