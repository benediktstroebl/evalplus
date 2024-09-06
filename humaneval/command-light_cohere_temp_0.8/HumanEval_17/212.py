```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    format_string = '{0:02}{}'

    beat_counts = {note: len(format_string.format(0) for note in notes})
    note_counts = {note: 4 for note in notes}

    return [beat_counts.format(format_string.format(0, note) for note in music_string.map(note_counts)]
```

The above Python script defines a function `parse_music` that parses a string representing musical notes in a specific format and returns a list of integers representing the number of beats of each note. It uses a legend of whole, half, and quarter notes, and defines a dictionary to map these to the number of beats each one lasts. 

The function then uses this dictionary to map each note in the input string to the number of beats it lasts.