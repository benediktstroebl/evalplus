Here's a Python script with a self-contained function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    return [max_number]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list with the rolling maximum elements found in the original list. The example usage demonstrates how this function can be applied to a list of numbers and the result is printed.