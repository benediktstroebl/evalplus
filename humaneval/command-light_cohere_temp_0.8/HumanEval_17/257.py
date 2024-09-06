```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')')
    music_info = {
        'o': 4, 'o|': 2, '.|': 1
    }
    notes = [int(note.strip()) for note in notes]
    return notes

# Test cases
test_str = 'o o| .| o| .| .| .| .| o o'   '
test_notes = parse_music(test_str)
print(test_notes)

test_str = 'o o o| o o .| o o'   '
test_notes = parse_music(test_str)
print(test_notes)

test_str = 'o o o o o o o| .o o'   '
test_notes = parse_music(test_str)
print(test_notes)

test_str = '.'*o
test_notes = parse_music(test_str)
print(test_notes)
```