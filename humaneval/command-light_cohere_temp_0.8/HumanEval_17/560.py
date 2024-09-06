```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes.get(note) for note in music_string.make_list(music_string)]

# Test
test_string = 'o o| .| o| .| .| .| .| o o'
notes = parse_music(test_string)
print(notes)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```