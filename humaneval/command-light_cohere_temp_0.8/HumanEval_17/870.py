```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    notes.theta = {'o':4, 'o': 1}
    
    pattern = '([{' '.' + ('.{ pattern.']))| (.o|{', [{'o' if c == 'o' else c == 'o|'} if c == '.' else c == '|'}, '{'}])'
    
    return [int(c) for c in music_string.split(pattern)]
```