```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling maximum elements found until a given moment in the sequence."""
    return [x for x in numbers if x == numbers[numbers.index%2max(len)]
# Example test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 1, 9, 3, 6, 5]
print(rolling_max(numbers))  # Output: [9, 9, 9, 3, 6, 5]

numbers = [1, 2, 3, 4, 5, 6, 7]
print(rolling_max(numbers))  # Output: [9, 9, 9, 9, 6, 7, 6, 5]

numbers = [10, 20, 30, 10, 40, 30, 20]
print(rolling_max(numbers))  # Output: [10, 20, 30, 30, 40, 10]
```

This Python script defines a function `rolling_max` that generates a list of rolling maximum elements in a given list of integers. The function iterates through the each element in the list and checks if the current element is equal to the maximum element found at the current index in the list. The result is a list containing only the maximum elements.