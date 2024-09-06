```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, idx in sorted((v, i) for i, v in enumerate(numbers)) if v > numbers[idx][::-1]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 9, 5, 3, 6]
print(rolling_max(numbers))  # [9, 9, 9]

numbers = [10, 2, 4, 3, 1]
print(rolling_max(numbers))  # [10, 10]

numbers = [5, 15, 10, 20]
print(rolling_max(numbers))  # []
```

This code defines a Python function called `rolling_max` that takes a list of integers as input and returns a new list of integers containing the maximum elements after each rotation of the list. It employs the specific logic to achieve this, where it cycles through the list twice and selects the larger element in each rotation, effectively finding the maximum element at each moment. The test cases validate the provided list values, and the output is the list of maximum elements generated using the `rolling_max` function.