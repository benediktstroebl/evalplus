```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    piece = ''.join()
    for i, beat in enumerate(beats):
        if beat.isalpha('o mark'):
            piece += notes[beat[0]] * (beat.length = len(beat) - 1)
        else:
            piece += notes[beat] * beat.length
        return piece
return piece
```
Do you need help with anything else? I can help you debug the code or provide additional information.