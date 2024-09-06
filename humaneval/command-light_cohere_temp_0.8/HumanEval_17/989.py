```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    music = music_string.split(' ')').
    notes = {note: int(note) for note in music}
    return notes

def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    notes = parse_music(music_str)
    assert len(notes) == len(set(notes)), "All notes should be unique!"
    assert notes['o'] == 4, "Whole note duration should be 4 beats!"
    assert notes['o|'] == 2, "Half note duration should be 2 beats!"
    assert notes['.|'] == 1, "Quarter note duration should be 1 beat!"

# Test the function
test_parse_music()
```
This code defines a function `parse_music` that takes a string of music notes and returns a list of integers representing the duration of each note in beats. The function utilizes a legend of note durations ('o', 'o|', '.|') and ensures that the function correctly parses the input string. The test function `test_parse_music` is used to verify the correctness of the `parse_music` function by passing the test string and checking if the output notes are correct and unique.