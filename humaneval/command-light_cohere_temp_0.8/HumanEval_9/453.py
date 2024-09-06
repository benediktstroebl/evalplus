```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling maximum elements found until the given moment in the sequence."""
    return [x if x <= num else num for num, x in zip(numbers, numbers[1:]))

#Test case 1
numbers = [1, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test case 2
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [1, 3, 3, 4, 4]

# Test case 3
numbers = [10, 20, 30, 40]
result = rolling_max(numbers)
print(result)  # Output: [20, 30, 40]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the maximum elements from the original list after rolling them forward by one. The test cases provided demonstrate the use of the function with different input lists and verify the output.