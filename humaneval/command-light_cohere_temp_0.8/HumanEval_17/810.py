```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = [1, 2, 1]

    for note, beat in zip(notes, beats):
        if note in music_string:
            start = music_string.find(note)
            if start == -1:
                length = len(music_string) - start
                return [beat] * length
            else:
                for start in range(len(music_string)):
                    if music_string[start] == note:
                        length = music_string[start+1 :].find(note)
                        break
                if length == 0:
                    return []
                return [beat] * length

    return []
```