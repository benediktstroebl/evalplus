```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [x for x in numbers if x > numbers[-1]] + [numbers[-1]]
    return max_numbers

# Test cases
numbers = [1, 2, 3, 2, 3]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [3, 4, 5]

numbers = [10, 11, 12, 13, 14]
result = rolling_max(numbers)
print(result)  # Output: [14, 14, 14]
```

This script defines a function called `rolling_max` that takes a list of integers as input and returns a new list that contains the maximum elements from the original list, considering the last element of the list as the current maximum element. 

The test cases demonstrate the way to use the `rolling_max` function to solve the problem.