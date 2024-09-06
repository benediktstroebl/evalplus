Here is a self-contained Python function that solves the problem you described: 

```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[c] for c in music_string.split(' '|')]
```

This function uses a dictionary `notes` to map musical notes to the number of beats that each lasts. It splits the strings into lists of notes using `split(' '|')` and then iterates over each note in the string and looks it up in the dictionary to find out how many beats it is supposed to last.