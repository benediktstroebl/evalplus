```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    return [notes[ch] for ch in music_string.get()]
```
This code defines a function parse_music that takes a music string as input and returns a list of integers. It uses a string parsing to split the input string into a dictionary of characters and their corresponding beat values, and then loops through the dictionary to extract the values corresponding to each character in the music string.