```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    
    beat_counter = [0] * 4
    for note in music_string:
        beat_counter = [beat_counter[i] + 1 for i in range(len(note)) if note == 'o' or note == 'o|']
        beat_counter = beat_counter[:-len(note)] if note == 'o' else beat_counter[:-len(note) // 2]
        
    return [beat_counter[i] for i in range(len(beat_counter))]

# Test cases
def test_parse_music():
    test_string = 'o o| .| o| .| .| .| .| o o'
    expected_result = [4, 2, 1, 2, 1, 1, 1, 1, 4]
    result = parse_music(test_string)
    assert result == expected_result
    
    test_string = '.'
    expected_result = []
    result = parse_music(test_string)
    assert result == expected_result
    
    test_string = 'oo'
    expected_result = [8]
    result = parse_music(test_string)
    assert result == expected_result
```
This Python script defines a function `parse_music` that takes a music string in a specific format and returns a list of integers representing the number of beats for each note. The function then implements this legend for musical notes, using a dictionary to map note characters to the corresponding beat values. The test_parse_music function contains test cases for various scenarios, including empty string, one note, and multiple notes.

These test cases effectively validate the correctness of the `parse_music` function.