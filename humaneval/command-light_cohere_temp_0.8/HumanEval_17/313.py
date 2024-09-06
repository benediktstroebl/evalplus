```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']  # ASCII characters for whole, half, and quarter notes
    beats = [4, 2, 1]  # Duration in beats

    notes = music_string.split()
     # The music_string is split into an array of characters, which are in turn the notes.
    notes = [notes + beats]  # Convert the notes into an array of beats, then add the beats.
    return notes

    ```This function splits the input music string into a list of ASCII characters, then creates a list of beats based on the characters. This beats list is the notes to be split into notes, and the notes to be added to the beats list.
```