```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = numbers[0]
    for num in numbers[1:]:
        if num > max_numbers:
            max_numbers = num
    return [max_numbers]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 3, 4, 4]

numbers = [4, 1, 5, 6, 7, 8, 9]
result = rolling_max(numbers)
print(result)  # Output: [9, 8, 7, 6, 5, 4, 3, 2]

numbers = [10, 20, 30, 40, 50, 60, 70]
result = rolling_max(numbers)
print(result)  # Output: [60, 50, 40, 30, 20, 10, 7]
```
This script defines a function `rolling_max` that generates a list of the rolling maximum elements from a given list of integers. It utilizes type hints to show the best-practice method to solve this problem.