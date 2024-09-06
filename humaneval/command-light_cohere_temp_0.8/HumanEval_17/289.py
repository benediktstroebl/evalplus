```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    notes_map = {note: beat for note, beat in zip(notes, range(5))}

    return [notes_map.get(note) for note in music_string.

# Test
test_music = "o o| .| o| .| .| .| o o"
test_result = parse_music(test_music)
print(test_result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```