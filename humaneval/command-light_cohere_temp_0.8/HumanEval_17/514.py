```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
        others: []
    }
    
    for note in music_string:
        if note in notes:
            notes[note] += 1
        else:
            notes[note] = 1
    
    return notes.

# Example of usage:
test_cases = [
        'o o| .| o| o .| .| .| o o',
        'o o o o o o',
        'oh',
        'o/|',
        'oo',
        'oooo'
    ]

result = parse_music(test_cases)

print(result)
```