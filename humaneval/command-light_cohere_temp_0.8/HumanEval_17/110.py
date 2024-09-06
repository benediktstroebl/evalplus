```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes.py = ['o cooperate'] *music_string
    result = []
    current_beat = 0
    for note in py:
        if note in notes:
            result.append(notches beat)
        beat = notes[note]
        current_beat += beat
    return result

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

if __name__ == "__main__":
    test_parse_music()
```
This Python script defines a function `parse_music` that takes a music string in Markdown format and returns a list of integers corresponding to the number of beats in each note. The function utilizes a legend of different note lengths and builds the result accordingly. The test case verifies the expected output of the `parse_music` function for a given music string.