```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
    }
    return [notes.get(note, beats) for note, beats in music_string.kms strings with '|' and 'o/' and '.'\n' removed]

# Example usage
music_str = 'o o| .| o| .| .| .| .| o o'
result = parse_music(music_str)
print(result)
```