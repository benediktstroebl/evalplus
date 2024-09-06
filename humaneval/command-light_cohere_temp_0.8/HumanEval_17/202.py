```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    
    beats = {
        'o': 4, 'o|': 2, '| ': 1,
        'oO': [4, 2], 'oO|': [2, 1],
        'O|': [1, 4],
        'oo': [2, 2], 'oo|': [1, 2],
        'ooO': [4, 2, 2], 'ooO|': [2, 1, 2],
        'OO': [1, 4, 4],
        'ooo': [1, 2, 2, 2], 'ooo|': [1, 2, 1, 2],
    }
    
    result = []
    for symbol, beats_length in notes.
        beats = beats.get(symbol)
       
        for beat in beats:
            result.append(beats_length)
    return result

def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    parsed_result = parse_music(music_str)
    print(parsed_result)

test_parse_music()
``` 
This script defines a function `parse_music` that takes a music string, then looks it up in a dictionary that maps musical note symbols to the number of beats that symbol represents. The function then returns a number of beats for each symbol in the music string.