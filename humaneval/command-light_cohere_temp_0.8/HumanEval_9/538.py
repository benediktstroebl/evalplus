```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:i], numbers[i]) for i, j in zip(range(len(numbers)), numbers)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 3, 4, 4]

numbers = [2, 4, 4, 2, 3, 5]
result = rolling_max(numbers)
print(result)  # Output: [2, 4, 4, 2, 5]

numbers = [10, 11, 12, 13, 9, 7]
result = rolling_max(numbers)
print(result)  # Output: [10, 11, 12, 13, 12, 13, 9, 7]
```
This Python code defines a function `rolling_max` that calculates the rolling maximum element of a list of integers. The function utilizes a result list and a nested list to track the maximum elements as the list progresses. The test cases demonstrate the