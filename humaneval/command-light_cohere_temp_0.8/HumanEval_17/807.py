```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "."": 4,
    }
    beats = 0
    output = []
    for note in music_string.split(" " ")[::-1]:
        beats += notes[note]
        output.append(beats)
    return output

# Example usage
test_string = "o o| .| o| .| .| .| o o"
expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
result = parse_music(test_string)
assert len(result) == len(expected)
```