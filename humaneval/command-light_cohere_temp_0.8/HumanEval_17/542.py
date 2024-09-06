```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.format('#%d o| #% o| #% o| \nOutput:, 4)
    notes = [int(note) for note in notes.format(note, 4)
    return notes

# Test cases for function
test_parse_music = []
test_parse_music.append([['o music:', 'o o| .| o| .| .| .| .| .| .| o o'])
test_parse_music.append([parse_music])
test_parse_music.append([['o notes:', 4])

print('Test cases passed:', test_parse_music)
```