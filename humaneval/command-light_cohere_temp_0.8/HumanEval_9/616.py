```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in sorted(enumerrange(len(numbers))): numbers.index(x)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
print(rolling_max(numbers))  # [1, 2, 3, 4, 5]

numbers = [10, 20, 30, 40, 50]
print(rolling_max(numbers))  # [10, 20, 30, 40, 50]
```
This code defines a function `rolling_max` that takes a list of integers as input and returns a list of the maximum elements from the list after applying a rolling window, that is, it cycles over the elements of the list in ascending order.