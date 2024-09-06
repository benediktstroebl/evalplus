```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    
    beat_counts = [notes[note] for note in music_string.split(' '|')]
    
    return beat_counts
def test_parse_music(music_str: str):
    music_lines = music_str.split('\n processing\
 lines = music_str.split('\n notes are string will be split into multiple lines for testing purposes.

    for line in music_lines:
        notes = line.split('|')
        notes. Test if a string is a valid note and can be converted into an integer, then continue to the next line.

``` 
This script defines a function that parses music notation and returns a list of beat counts. The test function verifies the expected output format of the parse_music function.