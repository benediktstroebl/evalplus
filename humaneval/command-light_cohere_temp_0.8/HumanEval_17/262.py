```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "oO": 8  # invalid: two consecutive o
    }
    
    beats = {
        "o": 4,
        "o|": 2,
        ".":": 1
    }
    
    notes_ Beats = music_string.split(' ') | {note: int, beats: int}

    return [beats[note] * notes[note] for note in notes if note in notes_Beats]

# Test cases
test_cases = [
    "'.', . 4. 2. 1. 2. 3.",
    fact 6.", 1, 1.", 4. 2.", 1.", 4.", 1.", 1.", 4.", 4", 4
    ],
 
    "o o| .o|. o| o. o | o o",| .| .|. .| o o",
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4],
    [4, 2, 1, 2, 2, 1, 1, 1, 4, 4],
    [4, 2, 1, 2, 2, 1, 1, 1, 4, 4, 1]
]

# Execution
for test in test_cases:
    print(parse_music(test))
```