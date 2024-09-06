```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beats = music_string.split(' ')
    ...[0] for i in range(len(beats) - 1) if beats[i] == 'o'
    return [notes[note] for note in music_string.split(' |')]
```
This function splits the music string by spaces and then loops through the characters of the split string. It returns a rhythm as the string "o o| .".