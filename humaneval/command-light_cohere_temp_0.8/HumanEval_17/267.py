```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beats = [1, 2, 1]

    notes = [item for item in music_string.split(' ')']
    time = []
    for note in notes:
        for beat in beats:
            if note.find(note) != -":
                time.append(beat)
                break
        return time
```
This Python function, parse_music, takes a string music_string as input and is responsible for parsing and returning a list of integers that represent the number of beats for each note in the music. The function utilizes a `notes` list containing the notes and `beats` list containing the beat lengths, then iterates through the `notes` list, splitting each string by a ' ' character. The function searches each note in the `notes` list using the `find()` method and, if it finds a match, appends the beat from the `beats` list. The function then loops through the time the list of beat numbers, each corresponding to the beat length found. The function then returns the time list, which contains the number of beats for each note in the music.