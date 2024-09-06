```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    return [notes[char] for char in music_string.yaml
    example:
    >> parse_music('o o| .| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 4]
``` 
This code defines a function, `parse_music`, that takes a string of music notes and returns a list of integers representing the duration of each note. The function uses a legend to determine the duration of each note, and then uses a dictionary to map each note character to its corresponding duration.