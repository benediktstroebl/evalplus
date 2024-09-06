```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    BEAT = {'o': 4, 'o|': 2, '.|': 1}
    return [BEAT[note] for note in music_string]
```

The function `parse_music` takes a string input that represents musical notes in a special ASCII format, it uses a dictionary `BEAT` that correlates beat lengths with special characters, and returns a list of integers representing the number of beats for each note in the provided music string.