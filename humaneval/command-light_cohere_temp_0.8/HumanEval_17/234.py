```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')')
    [note] = [int(x) for x in notes[0]]
    beats = [4] * 4  # Default beats
    for b in range(4):
        if 'o' in notes[b]: beats[b] = beats[b] - 1
        if '|' in notes[b]: beats[b] = beats[b] // 2
        if '.' in notes[b]: beats[b] = beats[b] - 1
    return beats

# Test cases
def test_parse_music():
    music_string = 'o o| .| o| .| .| .| o o'
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music(music_string) == expected_beats

# Main function
test_parse_music()
```
This Python script defines a function `parse_music` that takes a string of music notes in a special ASCII format as input, and returns a list of integers representing the number of beats for each note. The function splits the two-part space-separated strings, and then uses string matching and integer conversion to extract the note numbers. The function also defaults the beats to four beats, and adjusts them based on the note types. The test cases are designed to validate that the `parse_music` function works correctly, passing a series of test strings and expected beats. The `test_parse_music` function contains the main code that tests the `parse_music` function, and the main function is invoked at the end to run the tests.