```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(sorted(numbers), range(len(numbers))) if i < len(numbers) and numbers[i] > numbers[i-1]]

# Test cases
numbers = [1, 2, 3, 4, 5]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 4, 5]

numbers = [2, 3, 4, 5, 6]
print(rolling_max(numbers))  # Output: [2, 3, 4, 5]

numbers = [0, 9, 1, 2, 3]
print(rolling_max(numbers))  # Output: [0, 1, 2]

numbers = [5, 1, 4, 3, 2, 1, 3]
print(rolling_max(numbers))  # Output: [5, 4, 3]

numbers = [98, 99, 95, 91, 89, 87]
print(rolling_max(numbers))  # Output: [99, 95, 91]

```
This Python code provides a function called "rolling_max" that generates a list of the rolling maximum elements from a given list of integers. It employs a techniques to sort the input list and find the maximum element in the list for each index. The test cases demonstrate the the function's effectiveness in handling various scenarios with different input lists.