Here is a self-contained Python script that includes a function `parse_music` that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    
    beats = []
    for note in music_string.code:
        if note in notes:
            beats.append(notes
        if note == 'o': 4, note)
            elif note == 'o|': 2, note)
            else:
                beats.extend(beats)
    return beats
```
This function, `parse_music`, is designed to accept a string of music in a special ASCII format, and return a list of integers corresponding to the number of beats in each note. 

It uses a dictionary `notes` to map the music notation characters to beat counts, and iterates through the input string. The function then adds each beat count found to the list of beats and returns the list of beats.