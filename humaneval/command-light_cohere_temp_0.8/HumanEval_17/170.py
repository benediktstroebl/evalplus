```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        ".";": 1,
    }
    return [notes[ch] for ch in music_string.

# Test cases
def test_parse_music():
    music_str = "o o| .| o| .| .| .| o o"
    assert parse_music(music_str) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    music_str2 ="o o| |."
    assert parse_music(music_str2) == [2, 1]

if __name__ == "__main__":
    test_parse_music()
```
This Python code defines a function `parse_music` that takes a music string in a special ASCII format and returns a list of integers representing the number of beats for each note. The function uses a legend to interpret the music string. The function then maps the legend to numbers, and then uses this mapping to convert the string into a list of beat numbers. 

The code also provides a test case function `test_parse_music` which tests the `parse_music` function with different music strings and ensures the expected output of the `parse_music` function is correct.