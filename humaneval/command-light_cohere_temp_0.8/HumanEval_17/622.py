Here's a solution to the markdown music parsing problem:
```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    beats = [notes[note] for note in music_string.split('.')
    _ music_string.split('o Richards the framework:
    notes.
    beats.

    return beats

    return beats
```
This Python function called `parse_music` takes a string `music_string` representing musical notes in a special ASCII format. The function then creates a dictionary `notes` with keys representing notes and corresponding values representing the number of beats each note lasts. Then, the function iterates over each note in the `music_string` using string splitting with the `split` method. It checks each note against the string `notes` and assigns the corresponding beat value. 

This solution is a self-contained function that takes a string of music notes and returns a list of beats corresponding to the notes in the music.