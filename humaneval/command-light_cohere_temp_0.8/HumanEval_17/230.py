Below is a self-contained Python script that defines a function `parse_music` solving the markdown code block you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    pattern = r'(?:.)[o| (%[0-27])|o)'
    return [int(x) for x in re.match(pattern, music_string).
```

This function accepts a string representing music notes in a special ASCII format, and then maps the ASCII characters into integers, and uses the `re.then` module to match the string and return the list of integers corresponding to the number of beats each note lasts.