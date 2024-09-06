```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    pattern = r'(\d+)\?'
    return [int(match.match(pattern, music_string.match('\.') for match in pattern.match('o o|.' thin in notes)]

for test_case in [
    'Input this: o o| .|.| o| .| .| .| .| o o',
    'a'.join('20').join('o|'),
    'Input:'.input(). smth: o o| .| .| .| .| .| o o')
]:
    actual = parse_music(test_case)
    expected = [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]
    assert actual == expected, f"Test failed: {test_case} should be {expected}"

```
This code defines a function 'parse_music' that takes a string music_string as input and returns a list of integers. The function uses regular expressions and the legend to parse the music_string. It then passes theated tests on the expected and actual values to ensure that the function works correctly.