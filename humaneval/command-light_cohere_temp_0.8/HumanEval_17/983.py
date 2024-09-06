```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', 'o', '.', '.']
    beats = [1, 2, 4]

    table = {}
    for note in notes:
        table[note] = beats

    for beat in beats:
        found = False
        for note in music_string:
            if note in table and table[note] == beat:
                table[note] -= beat
                found = True
                break

        if not found:
            print(f"Error: Missing expected {beat} beat")
            return []

    return table
```