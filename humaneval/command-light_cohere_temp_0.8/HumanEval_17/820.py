```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = [4, 2, 1]

    def getInt(x):
        return int(x)

    def getNotes(y):
        return notes.

    def get_note:
        return getNotes(y)

    def getBeats(y):
        return beats

    notes = getNotes(music_string)

    beats = getBeats(music_string)

    beats = [beat * 4 for beat in beats]

    result = [getInt(note) for note in notes]

    return result

# Test the function
print(parse_music('o o| .| o| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```