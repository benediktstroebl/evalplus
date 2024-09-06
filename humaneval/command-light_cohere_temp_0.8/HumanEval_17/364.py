```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beat_counter = [0] * 4
    for symbol, beat in music_string.get(symbol, 'o').items():
        beat_counter[symbol] += 1
    return beat_counter

# Test case 1:
test_case1 = 'oo o| .| o| o| .| .| .| o o'  '
test_result = parse_music(test_case1)
assert len(test_case1) == len(test_result)
assert [0] == test_result[0]
assert [1] == test_result[1]
assert [2] == test_result[2]
assert [3] == test_result[3]
assert [4] == test_result[4]

# Test case 2:
test_case2 = 'oo o| o o| . . | .| o o' o o'  '
test_result = parse_music(test_case2)
assert len(test_case2) == len(test_result)
assert [0, 2] == test_result

# Test case 3:
test_case3 = 'oo o| .| o| . o' '
test_result = parse_music(test_case3)
assert len(test_case3) == len(test_result)
assert [0, 0, 0, 0] == test_result

# Test case 4:
test_case4 = 'o o| .| . o o' o o o'  '
test_result = parse_music(test_case4)
assert len(test_case4) == len(test_result)
assert [0, 4, 2, 6] == test_result
```

This code defines a function **`parse_music`** that takes a string in a specific musical notation format and returns a list of integers representing the beat count for each symbol in the music. The test cases cover various scenarios, and the function is expected to correctly parse the music strings and provide the corresponding beat counts.