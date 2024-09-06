```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = music_string.split(' ') | ['o']
    notes.
    return [ beats.
    # Arrange the. test the music string to the test data

# Example test:
music_string = 'o o| .| o| .| .| o o'
test_parse_music = parse_music(music_string)
print(test_parse_music)
```