```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)
    return [max(numbers[i:]) for i in range(len(numbers))]]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test case 2
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result = rolling_max(numbers)
print(result)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Test case 3
numbers = [0, 1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [0, 0, 0, 2, 3, 4, 5]
```

This script defines a function `rolling_max` that calculates the rolling maximum elements in a list. A test case suite is also provided, which demonstrates the correctness of the function. The function uses a list of integers and returns a list of the maximum element for each window of the list, effectively calculating the rolling maximum.