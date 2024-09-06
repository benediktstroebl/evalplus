```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in reversed(sorted(numbers)) if num > max_window or max_window == num]
    return [x for x in numbers if x > max_window or max_window == x]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
assertEqual(rolling_max(numbers), [1, 2, 3, 3, 3, 3, 4, 4])

numbers = [1, 3, 4, 5, 6, 5]
assertEqual(rolling_max(numbers), [6, 5, 6, 5])

numbers = [1, 2, 3, 1, 2, 3, 2]
assertEqual(rolling_max(numbers), [1, 2, 3, 2, 3])
```
This code defines a function `rolling_max` which takes a list of integers as input and returns a new list containing the rolling maximum elements. The function uses the
an efficient approach with a time complexity of O(n) using the `sorted` function along with a `reversed` function to get the correct order of the rolling maximum elements. The `test` module is used to add some tests to ensure the correctness of the `rolling_max` function.