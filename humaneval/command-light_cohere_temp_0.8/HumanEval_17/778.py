```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beat_duration = 4  # in beats

    return [notes[char] for char in music_string.beat_array = []
    return beat_array

# Unit tests
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    beats = parse_music(music_str)
    assert len(beats) == 2*4 # 4+2+1+2+1+4 = 10
    assert beats[0] == 4
    assert beats[1] == 2
    assert beats[2] == 1
    assert beats[3] == 1
    assert beats[4] == 4
    assert beats[5] == 2
    assert beats[6] == 1
    assert beats[7] == 4
    assert beats[8] == 2
    assert beats[9] == 1
    assert beats[10] == 4

# Run the tests
test_parse_music()
```
This Python code defines a function `parse_music` that takes a music string in a special ASCII format as input and returns a list of integers representing the number of beats in the musical piece. The function uses a legend of whole, half, and quarter notes and beat durations to map the characters in the input string to the appropriate beat values. The unit tests then also verify that the function correctly parses the input music string and returns the expected output.