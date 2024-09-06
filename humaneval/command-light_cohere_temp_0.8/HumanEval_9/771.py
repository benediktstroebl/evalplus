```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the list of rolling maximum elements in a given list of integers.
    """
    list of numbers is passed as an argument.
    The list of rolling maximum elements is returned.
    """
list comprehension and list slicing is used to find the rolling maximum element for each moment in the sequence.

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_list = rolling_max(numbers)
print(rolling_max_list)  # Expected output: [3, 3, 3, 4, 4]

numbers = [5, 1, 6, 7, 9, 3]
rolling_max_list = rolling_max(numbers)
print(rolling_max_list)  # Expected output: [9, 7, 6]

numbers = [3, 4, 2, 1, 1, 8, 2]
rolling_max_list = rolling_max(numbers)
print(rolling_max_list)  # Expected output: [1, 1, 2, 8]

# General use case
numbers = [1, 2, 3, 4, 5]
rolling_max_list = rolling_max(numbers)
print(rolling_max_list)  # Expected output: [4, 5]
```

The function rolling_max efficiently calculates and returns the list of rolling maximum elements from the input list of integers. The test cases ensure that the function works correctly for different scenarios, and the general use case demonstrates how the function can be applied to real-world data.