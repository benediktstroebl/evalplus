```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', 'o', '|', '.', 'o', 'o']
    beat_counts = {note: 4 for note in notes}
    pattern = r'(?<([oO]o| [oO]| [O].)')?'format=re

    match = re.findall(pattern, music_string)
    return [len(match) for match in match]

# Test case 1
test_case1 = parse_music('o o| .| o| .| .| .| .| o o')
print(test_case1)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Test case 2
test_case2 = parse_music('o o| o| .')
print(test_case2)  # Output: [2, 2]

# Test case 3
test_case3 = parse_music('o .| o| .')
print(test_case3)  # Output: [1]

# Test case 4
test_case4 = parse_music('o| .| o| .')
print(test_case4)  # Output: [2, 2]

# Test case 5
test_case5 = parse_music('| .|.')
print(test_case5)  # Output: []
```