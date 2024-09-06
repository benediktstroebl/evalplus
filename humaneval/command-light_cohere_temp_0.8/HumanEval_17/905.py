```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o|' : 4}
    beats = music_string.split('|')
    music_blocks = []
    for beat in beats:
        music_block = beat.split(' ')
        music_block = [note for note in music_block.split('o music_char if note in notes]
        music_blocks.append(music_block)
    return music_blocks
```