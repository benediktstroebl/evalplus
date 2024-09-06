```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sorted = sorted(numbers)
    rolling_maxes = []
    while True:
        small = numbers[0]
        for num in numbers[1:]:
            if num < small:
                small = num
        rolling_maxes.append(small)
        break
    return rolling_maxes

test_rolling_max = [ [-2, 3, 2, -5, -7, 1], [2, -3, 4, 8, 3, 10], [5, 6, 7, 9, 10], [1, 3, 2, 3, 4]]

assert rolling_max(test_rolling_max) == [1, 2, 3, 3, 4]

```