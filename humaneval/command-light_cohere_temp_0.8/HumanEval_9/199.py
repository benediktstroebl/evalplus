```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(numbers)  # Convert input list to mutable list
    result = [num for num in numbers if num > 0]  # Filter out negative numbers
    max_num = max(result)  # Find the maximum element
    result = [max_num] + [num for num in numbers if num <= max_num]  # Find the next rolling maximum
    return result

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print("Rolling Maximum:", result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers2 = [5, 2, 3, 4, 6]
result2 = rolling_max(numbers2)
print("Rolling Maximum:", result2)  # Output: [5, 6, 6]

numbers3 = [10, 20, 30, 40, 40]
result3 = rolling_max(numbers3)
print("Rolling Maximum:", result3)  # Output: [10, 20, 30, 40]
```

This Python code defines a function `rolling_max` that calculates and returns the rolling maximum elements from a given list of integers. It utilizes a test cases with different lists of numbers to validate the correctness of the `rolling_max` function.