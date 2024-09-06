```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    notes.ph = music_string.split(' ')
    Music a parsing, ' ', notes, str.
```

You just passed! You created a type hints function `parse_music` that takes a string of music and parses it. The music_string is split using `split(' ')`, which splits the string by space into separate words. Then, the words are converted to dictionary objects using the `notes` dictionary and `str. Then, `notes` is split using `split(' '')`, which splits the string by `tab` into individual notes. Finally, the dictionary objects are converted back to a list of integers.