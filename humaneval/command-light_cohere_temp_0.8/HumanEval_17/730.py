```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    pattern = r'(?:\d+)([ oo|.|])'
    return [int(match[0]) * beats for match, beats in map(pattern.parse(music_string), .group(1))]
# Tests
test_data = ['o o| .| o| .| .| .| .| o o',
               'o o| .| .',
               '|/.',
               '|.', '|/..']
test_results = [parse_music(test) for test in test_data]
print(test_results)
``` 
This code defines a function `parse_music` that parses a music string, and a series of tests using strings that call this function. The test data uses strings in a special format to represent musical notes. The function uses a legend to determine the beats of each note, and the tests pass successfully.