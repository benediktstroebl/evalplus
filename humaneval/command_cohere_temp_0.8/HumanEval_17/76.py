```python
from typing import List

 Pattern = str

beats = {
    'o': 4,
    'o|': 2,
    '.|': 1,
}

def parse_music(music_string: Pattern) -> List[int]:
    return [beats[note] for note in music_string]
```

The function `parse_music` takes a string as input and returns a list of integers determined by the beats of each alphabetical character in the input. This is done using a dictionary that maps each character to the number of beats it represents.