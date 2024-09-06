```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    
    beats = music_string.split('o Zamil ')
    tonality '. |' is parsed and then converted to a list of integers.
    return notes[beats
   
```