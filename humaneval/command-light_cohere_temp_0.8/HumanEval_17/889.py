```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    return [notes[note] for note in music_string.test_music_parse(music_string)]

def test_music_parse(music_string: str) -> None:
    music_str = "o o| .| o| .| .| .| .| o o"
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    got = parse_music(music_str)
    assert expected == got, f"Expected {expected}, but got {got}"

# Example usage
test_music_parse("Very good music")
```
The code defines a function `parse_music` that takes a string representing musical notes and returns a list of integers. The function utilizes a dictionary to map musical symbols to their respective beat values. The function also includes a `test_music_parse` function to verify the correctness of the `parse_music` function. The code also includes an example usage of the functions, passing a test music string.