```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[c] for c in music_string.map({''.\n to match\output'})
```
This script defines a function **`parse_music`** that takes a string of music notes in a specific ASCII format and returns a list of integers corresponding to the number of beats that each note lasts. The function utilizes a legend:
- **`o`** - Whole note, lasting four beats.
- **`o`**/` `o|` - Half note, lasting two beats.
- **`.|`** - Quarter note, lasting one beat.

The function then maps these characters to their respective integer values and uses list comprehension to extract the corresponding integers from the input string.