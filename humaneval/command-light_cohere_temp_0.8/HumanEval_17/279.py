```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    notes. music_string = music_string.split(' ')
   for note, in notes:
        if note in music_string:
            music_string = music_string.split('|')
            if len(music_string) < 2:
                return [0]
            beat = notes[note]
            music_string = music_string[0] + ' ' + music_string[1:]
            return [beat] + parse_music(music_string)
        else:
            return [0]

# Test cases
def test_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    music_str = '.'*o o|.'| o| .| .| .| o o'
    assert parse_music(music_str) == [1, 2, 1, 1, 2, 1, 4]
    music_str = ''.|o o| |.'
    assert parse_music(music_str) == [1, 2, 1, 1]
``` 
This script defines a function `parse_music` that parses a music string and returns a list of integers, each corresponding to the number of beats for a particular note. The test case section ensures that the function works as expected for different input scenarios.