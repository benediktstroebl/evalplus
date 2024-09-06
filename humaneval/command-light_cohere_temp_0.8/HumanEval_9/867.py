```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)  # sort the list of numbers
    max_num = numbers[0]
    current_max = max_num
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max:
            current_max += 1
    return [current_max, current_max + 1]

# Test cases
test_rolling_max = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
]

results = {}
for test in test_rolling_max:
    test_results = rolling_max(test)
    results[test] = test_results

for num, expected in results.
```