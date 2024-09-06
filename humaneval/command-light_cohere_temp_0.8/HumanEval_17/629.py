```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.': 1
    }
    return [notes[note] for note in music_string.test_music_parse_music("oo o| o| o| o| o| o| .| o o o")
```
This Python function, `parse_music`, takes a string music_string as input and returns a list of integers. The function utilizes a legend of notes in music, where 'o' stands for a whole note that lasts four beats, 'o|' for a half note that lasts two beats, and '|' for a quarter note that lasts one beat. It iterates the
          ASCII music notation, where the notes are read and their corresponding beat counts are stored in a dictionary for easy access.