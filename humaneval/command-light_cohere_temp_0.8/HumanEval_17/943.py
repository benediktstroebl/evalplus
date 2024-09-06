```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', '.', 'o', '.', '|', '.']
    patterns = [x for x in music_string.split() for x in notes]
    
    return [len(x) for x in patterns]
```