Here is a self-contained Python script that defines a function `parse_music` solving the problem:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = []
    current_beat = 0
    for note in music_string.strip():
       
        note:
        if note in notes.
        beat.append(current_beat)
        current_beat += notes[note])
        beats.append(current_beat)
        current_beat = 0
    return beats

# Test cases
def test_music():
    music_str = 'o o| .| o| .| .| .| o o'
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    return parse_music(music_str) == expected_beats

if __name__ == "__main__":
    print(test_music())
```

This script defines a `parse_music` function that takes a music string, and returns a list of beats that it represents. The music string is a list of characters that represent notes, and the function uses a dictionary to map those characters to the number of beats that they represent. The function then loops through the string, and for each character, appends the current beat to the list of beats, and increments the current beat. The test cases define a music string that is to be parsed, and the expected output of the `parse_music` function. The test cases then pass the expected output, and the `test_music` function is used to test the `parse_music` function.