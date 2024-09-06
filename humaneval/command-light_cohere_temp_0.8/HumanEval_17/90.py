```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    beats = []
    for note in music_string.get(note, '.' whole' if note in notes else note.

    beats.append(beats[-1])
    beats.append(beats[-1])

    return beats
```
This function takes a string of music as an input, where the music string represents a sequence of notes. The function then uses a dictionary to map the musical notes to the beats they last for. The function then iterates over the notes in the string and uses the get() method to extract the last note and appends it to the previous beat.