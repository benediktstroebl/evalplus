```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    BEAT = {'o': 4, 'o|': 2, '.|': 1}
    return [BEAT[note] for note in music_string]
```

The function `parse_music` takes a string as input and returns a list of integers determined by the beat lengths of the corresponding notes. This is achieved through a dictionary `BEAT` that maps note patterns to beat lengths. 

This solution works by first creating a dictionary that maps each possible note (by its pattern) to its corresponding beat duration, which is then used in a list comprehension that iterates through each note in the input string, picking its corresponding duration from the dictionary.