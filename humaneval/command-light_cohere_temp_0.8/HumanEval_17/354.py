Here is a self-contained Python function that parses and converts a musical notes string to a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    def parse(music):
        beats = {'o': 4, 'o|': 2, '.|': 1}
        result = []
        current_beat = 0

        for note in music:
            if note in beats:
                result.append(current_beat + beats[note])
                current_beat += beats[note]
        return result
```

This function uses a nested loop to iterate over each note in the music string. It uses a `beats` dictionary to map the notes to the number of beats each one lasts. The function returns a string corresponding to how many beats does each note last.