Here's a self-contained Python function that solves the markdown code music parsing problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    return [notes[note] for note in music_string.code_4.split('|')
    Dryly split the strings using '|' as separator, then loop through this list and map the notes to their respective beat counts.

# Examples
music_string = 'o o| .| o| .| .| .| o o'
result = parse_music(music_string)
print(result)  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```