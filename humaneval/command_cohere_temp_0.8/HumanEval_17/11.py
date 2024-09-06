```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Use regex to find all whole, half and quarter notes in the string
    beat_patterns = {'whole': re.compile(r'o'), 'half': re.compile(r'o|'), 'quarter': re.compile(r'.|')}
    beats = ['whole', 'half', 'quarter']  # Sorted order of notes

    result = []
    for i, note_type in enumerate(beats):
        for m in beat_patterns[note_type].finditer(music_string):
            result.append( BeatCounter.note_beat_mapping[note_type] )

    return result
```

The BeatCounter class is introduced to encapsulate the beat mapping and the parsing logic which is later used in the `parse_music` function. This makes the code more modular and easier to understand.

```python
class BeatCounter:
    note_beat_mapping = {
        'whole': 4,
        'half': 2,
        'quarter': 1,
    }

    def __init__(self):
        self.beat_patterns = {'whole': re.compile(r'o'), 'half': re.compile(r'o|'), 'quarter': re.compile(r'.|')}

    @staticmethod
    def parse_music(music_string: str) -> List[int]:
        beats = ['whole', 'half', 'quarter']  # Sorted order of notes
        result = []
        for i, note_type in enumerate(beats):
            for m in BeatCounter.beat_patterns[note_type].finditer(music_string):
                result.append( BeatCounter.note_beat_mapping[note_type] )
        return result
```