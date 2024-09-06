```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    pattern = r'(\d+)?\d+(?:[oOoO|])(\d+)'
    return [int(match[0]) for match in re.findall(pattern, music_string)]

# Test the function
test_music = "o o| .| o| .| .| o o"
expected = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
result = parse_music(test_music)
assert len(result) == len(expected)
assert result == expected
```
This code defines a function `parse_music` that parses a music notation string and returns a list of note lengths. The function uses a legend of musical notes and a regular expression to extract the note lengths from the string. 

The test case uses the same music string and checks if the function's output matches the expected result.