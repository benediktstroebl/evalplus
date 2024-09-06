```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)  # Convert input to list
    return [max(numbers[i:i+1]) for i in range(len(numbers))]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 3, 4, 4]

numbers = [3, 1, 9, 2, 10, 100]
result = rolling_max(numbers)
print(result)  # Expected output: [9, 10, 100]

numbers = [100, 101, 102, 103]
result = rolling_max(numbers)
print(result)  # Expected output: [100, 101, 102]
```

This script defines a function `rolling_max` that calculates the rolling maximum elements from a given list of integers. The function first converts the
the input list into a single list of elements, and then uses a generator expression to find the maximum element for each window of the list, starting from the beginning of the list. 

It then returns the resulting list of rolling maximum elements.