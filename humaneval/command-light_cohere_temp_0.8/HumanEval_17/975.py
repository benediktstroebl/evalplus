```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', '.']
    beats = 4
    return [beats * len(notes) // len(music_string) for _ ,note in enumerate(music_string.split('\n.split('|') ][::-1])
```
The function takes a string of music and returns a list of integers corresponding to the number of beats of each note. 

This solution defines a list of music note characters, each representing a whole, half, or quarter note. The function uses the legend to split the string into a list of notes, then performs a simple calculation to get the number of beats for each note.