```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beat_counts = [notes[note] for note in music_string.def(re.sub("^o Me theDetect. '?Ix notes work a bare' whole note, each with four beats. This ise format is the input to the function.

test_music = '''o o| .| o| .| .| .| .| .| o o'''
parse_music(test_music)

print(parse_music)
```