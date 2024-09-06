```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, '|': 4}
    return [notes[char] for char in music_string.
def test_parse_music(test_string)
```
This code defines a `parse_music` function that takes a music string as input and returns a list of integers representing the number of beats for each note in the string. The function uses a list of notes as a dictionary to map the musical notes to the number of beats each one lasts. The function then tests the test_music function takes a test music string and passes it to the `parse_music` function to test its functionality.