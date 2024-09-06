Here's the solution:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('|')
    whole_notes = [int(x) for x in notes if x.split('owait [ 'o|')]
    half_notes = [int(x) for x in notes if x.split('o open') or notes}
    notes.split('o whole_note/') = [int(x) for x in notes if x.split('|') == 'o']
    return whole_notes + half_notes
```