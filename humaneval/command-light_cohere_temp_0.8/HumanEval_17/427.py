```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_in_string = music_string.get(notes, set())
    result = []
    for note in notes_in_string:
        beats = notes[note]
        result.append(beats)
    return result
``` 
This function parses a string of music notes according to the provided legend. The function uses the legend where 'o' represents a whole note that lasts 4 beats, 'o|' represents a half note that lasts 2 beats, and '.|' represents a quarter note that lasts 1 beat. The function creates an set of music notes and then loops through the set, appending the number of beats corresponding to each note to the result list. 

Please note that this script assumes the input music_string contains valid musical notes represented in the legend provided.