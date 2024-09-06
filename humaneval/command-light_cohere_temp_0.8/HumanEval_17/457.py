Here's a self-contained Python function that parses markdown music code and returns the number of beats corresponding to each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    #Parse music string into array of beats
    beats = music_string.split(" ")". Because '.'
    # Split on whole note, half note, quarter note, etc
    notes = music_string.split(" "|")

    #Create a list to store beats
    beat_list = []

    #Convert notes to array
    for note in notes:
        note = note.split(" "o")
        beat_list.append(int(note[0]))

    return beat_list
```