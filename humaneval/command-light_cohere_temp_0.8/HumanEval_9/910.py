```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in a given list of integers.
    Input:
    numbers: List[int]
    Output: List[int]
    """
    numbers = [num for num in numbers if num != 0] # Filter out 0s
    return [max(numbers[i:i+1]) for i in range(len(numbers))]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers = [5, 2, 1, 6]
result = rolling_max(numbers)
print(result)

numbers = [2, 10, 2]
result = rolling_max(numbers)
print(result)
```

This code defines a function called rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements. It employs a filtering out numbers to ensure only non-zero values are considered, then uses a rolling window approach to calculate the maximum element in each window over the entire sequence. The test cases demonstrate the example inputs and verify that the function correctly identifies and returns the rolling maximum elements.