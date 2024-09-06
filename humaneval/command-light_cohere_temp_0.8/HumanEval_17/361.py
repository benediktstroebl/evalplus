```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = 4  # 4 beats in a whole note
    format = '{:02}{}'  # to generate notes and beats in string format
    
    # split string into individual notes with their respective beats
    formatted_notes = [format.format(note, beats) for note in notes]
    
    notes = [int(note) for note in formatted_notes]  # convert string notes into integers
    
    return notes
```