```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, index in reversed(sorted(numbers)) if numbers[index] > num]

# Test case 1
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result) == 5, "Result is not 5-length"
assert sorted(result) == [5, 4, 3, 2, 1]

# Test case 2
numbers = [10, 9, 8, 7, 6]
result = rolling_max(numbers)
assert len(result) == 5, "Result is not 5-length"
assert sorted(result) == [10, 9, 8, 7, 6]

# Test case 3
numbers = [0, 1, 2, 3, 4]
result = rolling_max(numbers)
assert len(result) == 5, "Result is not 5-length"
assert sorted(result) == [0, 0, 1, 2, 3]
```
This script defines a function `rolling_max` that generates a list of the maximum elements from the beginning of a given list, testing it with three cases.