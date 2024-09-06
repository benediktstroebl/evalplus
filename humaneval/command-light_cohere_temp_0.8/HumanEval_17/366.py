Here is a self-contained Python script that solves the problem of parsing music notes in a string and returns a list of integers representing the duration of each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    def parse_notes(notes: str) -> List[int]:
        notes = notes.split('|')
        pattern = ['o', 'o|', '|', '.']
        result = []
        for item in notes:
            item = item.split(' ')
            beat = [int(x) for x in item]
            result.append(beat[0])
        return result
    return parse_notes(music_string)
``` 
This script provides a parse_music function that accepts a string music_string as input, which represents a series of music notes with their durations. The parse_notes function takes this music string and splits it by "|", creating a list of note names. The function then iterates over each note and splits it into a list of individual beats, which are then added to the result list, with the beat count being the first element.