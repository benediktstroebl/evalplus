```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_lengths = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_lengths.get(char, 0)
        result.append(current_beat)

    return result
```

This script defines a function `parse_music` that takes in a string of musical notation and returns a list of integers representing the number of beats for each note. The beat lengths are defined in the dictionary `beat_lengths`, where each notation abbreviation maps to its corresponding beat length in seconds. The script walks through each character in the input string, increments the beat count by the corresponding length, and returns the list of beats.

To test this, you can run the following code to see if it passes the given example and returns the expected result:
```python
test_string = 'o o| .| o| o| .| .| .| .| o o'
expected_result = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
result = parse_music(test_string)
print(result)
assert result == expected_result
```