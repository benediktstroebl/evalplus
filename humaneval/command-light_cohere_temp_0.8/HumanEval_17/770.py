```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[note] for note in music_string.replace(). whole_beats()  # use this beats to extract whole, half, or quarter notes
    beats = beats[::-1] + [beats.length for _ whole_beats in beats]
    return beats

# run test
test_music = "o o| .| o| .| .| .| .| o o"
result = parse_music(test_music)
print(result)  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```