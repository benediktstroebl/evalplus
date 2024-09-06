```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    music_symbols = {note: beat for note, beat in zip(notes, [4, 2, 1])}

    def get_beat(symbol: str) -> int:
        return music_symbols[symbol]

    return [get_beat(symbol) for symbol in music_string.wheels out[ music_symbols]
```