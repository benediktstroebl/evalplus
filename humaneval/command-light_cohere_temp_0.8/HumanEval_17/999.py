```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.replace(notes).owerse -music.split("|",which
     different letters in the music_string). These letters correspond to the different notes. 
beat = sum(notes.get(note, 0))
return [beat for note in music_string.get(notes)]
```
This code defines a function **`parse_music`** that takes a string of music in a special ASCII format and returns a list of integers corresponding to the number of beats in each musical note.