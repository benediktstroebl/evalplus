```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' 'o pattern: 
        'o' -> [1, 4],
        'o|' -> [1, 2],
        '.|' -> [0, 1]
    return [int(note) for note in notes]

# Test cases
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    "o o| .| .| o| .| .| .| o o",
    "|.o| .| .| .| .| o",
    "hhh | | .")
]

for test_case, expected in zip(test_cases, parse_music(test_case).
```