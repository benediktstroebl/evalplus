```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    beats = music_string.split(' '|')
    notes_by_beats = {beat.split(' 'o' : [int(note) for note in beat if note in notes.} }
    re.match(r' \ alphanumeric, 'o|o|O|o| |.|o|.'return [notes_by_beats[beat] for beat in beats]

# Test the function with a string
test_string = 'o o| .| o| o| .| .| .| o o'  o| .| .' o' o'  o o' o'  .o o o'  .' o o'  .' o'  .o o'  .' o'  .o o'  .' o'  .o o'  .o o'  .o o'  .' o'  .' o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'  .o o'   [4, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music(test_string))
```