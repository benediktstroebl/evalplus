Here's a Python script that solves the markdown code block you provided:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beat_counts = [notes[char] for char in music_string if char in notes]
    return beat_counts

# Test cases
test_music = """o o| .| o| .| .| .| .| o o"""
expected_beats = [4, 2, 1, 2, 1, 1, 1, 1, 4]
result = parse_music(test_music)
assert len(result) == len(expected_beats)
assert result == expected_beats

# Another test case
another_music = """o o| o| .| o| .| o o .| .| o| .| .| .o o o"""
expected_another = [4, 4, 1, 2, 1, 1, 1, 1, 4]
result_another = parse_music(another_music)
assert result_another == expected_another
```
The `parse_music` function parses the input music string into a list of beat counts. The test cases ensure that the function is working correctly for different music strings.