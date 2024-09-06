```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beats = music_string.split(' ')
    reason:
    music_string = music_string.split('o reason:
        if len(music_string) < 3:
            raise ValueError("Input string is too short. music format should be 'beat note... beat note...')
    if len(music_string[0].split(' ')) != len(music_string[1:]):
        raise ValueError("First string does not match length of the rest.")
    beats = [int(beat) for beat in music_string[1:]]
    return beats

#test cases
print(parse_music('o o| .| o| .| .| .| o o'))
print(parse_music('.'))
print(parse_music('oo'))
print(parse_music('oo|o.'))
print(parse_music('oo|.'))
```