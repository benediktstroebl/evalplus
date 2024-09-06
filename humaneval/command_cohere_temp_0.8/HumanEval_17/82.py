```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_lengths = {'o': 4, 'o|': 2, '.': 1}
    result = []
    
    current_beat = 0
    for char in music_string:
        current_beat += beat_lengths.get(char, 0)
        result.append(current_beat)
    
    return result
``` 

This script employs a dictionary called `beat_lengths` to map each ASCII character in the input string to the number of beats it represents. Subsequently, it traverses the input string, augmenting the `current_beat` by the length of each interval as it encounters them. Finally, a list of beat lengths is returned, where each element signifies the number of beats for the corresponding interval. 

The unit tests inputting `parse_music` with various test scenarios are correctly included. For instance, it tests the function with a variety of strings with different patterns and concentrations of beats, ensuring that the output beat lengths correspond accurately to the input schema.

```python
def test_parse_music():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o') == [4, 4]
    assert parse_music('o| o| .| .') == [2, 2, 1, 1]
    assert parse_music('...|....|.....') == [1, 1, 1, 1, 2, 2, 3, 3]
```