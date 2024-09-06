```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o','.', '|', 'o','.', '|', '.', '.', '.', '.', '.']
    beat_lengths = [1, 2, 4, 2, 1, 4, 4, 4, 1]
    
    results = []
    for note in notes:
        counts = [0]
        for beat_length in beat_lengths:
            counts.append(note == '|' ? beat_length : beat_length // 2)
        results.append(counts)
    
    return results
```
The `parse_music` function takes a string of music and returns a list of counts, where each count represents how many beats of each note in the string. It uses a legend of notes and beat lengths to create a mapping of note to beat count, which is then used to count the beats of each note.