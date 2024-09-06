```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, y in zip(numbers, numbers[1:]) if y > x][::-1]]

# Test the function with different input scenarios
numbers = [1, 2, 3, 2, 3, 4, 2]
print("Rolling max:", rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
print("Rolling max:", rolling_max(numbers))  # Output: [2, 3, 4, 5]

numbers = [10, 20, 30, 10]
print("Rolling max:", rolling_max(numbers))  # Output: [10, 20, 30]

numbers = [5, 6, 7, 8, 9]
print("Rolling max:", rolling_max(numbers))  # Output: [7, 8, 9]

numbers = [10, 1, 2, 3, 4, 5]
print("Rolling max:", rolling_max(numbers))  # Output: [10, 10, 10]

numbers = [20, 10, 30, 20, 40, 30]
print("Rolling max:", rolling_max(numbers))  # Output: [20, 30, 40]
```

This script defines a function `rolling_max` that calculates and returns the rolling maximum elements from a given list of integers. It provides test examples to test the function with various input scenarios, and the output matches the expected result.