```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o iconic notation
    || harpsichord score to regular list
    return [beat * 4 for beat in map(note.split('|') for note in notes)]

# Example usage
music_str = 'o o| .| o| .| .| .| .| o o'
notes = parse_music(music_str)
print(notes)  # expected output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```