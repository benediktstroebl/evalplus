```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}  # Map of note names to duration
    beats = music_string.split(' ')'.  # Extract all beat strings. Then convert to integers
    whole note, half note, quarter note.
    return [notes to be a list of beat numbers, then multiply by the corresponding note duration from the notes dictionary.
```

print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 1, 4, 4]
```