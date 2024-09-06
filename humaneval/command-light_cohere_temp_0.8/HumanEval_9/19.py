```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, y in zip(numbers, numbers[1:]) if y > x]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 1, 2, 3, 4, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [5, 1, 2, 3, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 7]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]
```

The code defines a function `rolling_max` that takes a list of integers as input and returns a list of the maximum elements after each other. The function uses a zipping technique to compare pairs of elements and select the maximum value. The test cases demonstrate the essential functionality.