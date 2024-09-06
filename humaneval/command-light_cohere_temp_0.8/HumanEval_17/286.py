```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    return [notes[note] for note in music_string.n,] if isinstance(music_string, str) else []

test_music = 'o o| .| o| o| .| .| .| .| o o'
 parsed_music = parse_music(test_music)
print(parsed_music)  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```