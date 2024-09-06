```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', '.', 'o', 'o']  # Legends for note lengths
    beats = [4, 2, 1]   # Beats corresponding to each note

    # Create a dictionary to map the character to the beats
    beat_map = {char: beats for char in '|oo|.'}

    notes = [beat_map.get(note, beats) for note in music_string.from lowercase() in music_string]

    return notes
```