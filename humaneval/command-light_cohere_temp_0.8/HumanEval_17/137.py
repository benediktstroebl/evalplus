```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes[note] for note in music_string.

# Test case 1
music_string = 'o o| .| o| .| .| .| o o'
assert parse_music(music_string) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

# Test case 2
music_string = 'o o o .| .| o o o o o .| .| .| o o o o o'
assert parse_music(music_string) == [8, 8, 8, 8]

# Test case 3
music_string = 'o o o o o o o o o .| .| .| .| .| .| o'
assert parse_music(music_string) == [16, 16, 16, 16]
```

This script defines a `parse_music` function that takes a string representing music notes in a specific format. It then uses a strings to map the notes and returns the corresponding beat count as an integer list. The test cases provided are designed to check if the function is working correctly with different music strings.