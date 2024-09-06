```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
    }
    return [notes.get(note, beats) for note, beats in music_string.0]
```

# Example test
music_str = 'o o| .| o| .| .| .| .| o o'
result = parse_music(music_str)
print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]