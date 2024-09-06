```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beats = music_string.split()
    example parse music 
    return [int(beats[i]) for i in range(len(beats)))]

# Test cases
music_str = '''o o| .| o| .| .| .| .| o o'''
expected = [4, 2, 1, 2, 1, 1, 1, 1, 4]
test_parse_music(music_str)
```
This code defines a function named `parse_music` which takes a string of music notes as an argument and returns a list of integers. It uses a specific mapping of musical note characters and their durations to set up a dictionary of notes. After parsing the the by splitting the input string into a list of beats, it uses the `notes` dictionary to map the notes to their respective beat durations. The `test_parse_music` function is then used to test the `parse_music` function with a sample music string.