```python
from typing import List

beats = {'o': 4, 'o|': 2, '.': 1}

def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip().split('|')
    for n in notes:
        result.extend([beats[c] for c in n if c in beats])
    return result
```

The script utilizes a dictionary called beats that maps each musical notation to its corresponding number of beats. The `parse_music` function accepts a string of musical notation and returns a list of integers representing the number of beats for each note. It does this by first stripping any leading or trailing vertical bars ('|') from the input string and then splitting the string of musical notation into a list of vertical bar-separated strings. Subsequently, it iterates over each element and extends the result list with the corresponding number of beats for each note using the beats dictionary.

To test this, we can run the following code:
```python
test_list = ['o o| .| o| o| .| .| .| .| o o', 'o| .| o| o| .| .| .| o', 'o o| .| o| .| .| o| o']
expected_list = [
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4],
    [2, 1, 1, 2, 1],
    [4, 2, 1, 1, 1, 2]
]

for test, expected in zip(test_list, expected_list):
    assert parse_music(test) == expected
```
Each test case corresponds to a known correct result, so passing these to the function verifies that it behaves as expected. 
If you would like more details on the logic or the tests, feel free to ask!