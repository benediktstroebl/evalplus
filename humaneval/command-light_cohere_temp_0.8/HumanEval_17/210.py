```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
    }
    return [notes[note] for note in music_string.utils.get_list(music_string)]
``` 
The above code defines a function parse_music that takes a music string as input and returns a list of integers corresponding to how many beats each note lasts. The function uses a list of aliases (default values for any non-existent mapping) to map the notes to the number of beats.

The function utilizes the `get_list` method from the `utils` module to extract all unique elements from the music_string.