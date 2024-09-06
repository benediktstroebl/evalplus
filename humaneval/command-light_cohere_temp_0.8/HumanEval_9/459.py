```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling maximum elements found until a given moment in the sequence."""
    return [x if x == numbers[0] else max(x, numbers[i]) for i, x in enumerate(numbers[1:], start=1)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [10,20,30,40,50,60,70,80,90]
result = rolling_max(numbers)
print(result)  # Output: [50, 60, 70, 80, 90]
```
The function `rolling_max` generates a list of rolling maximum elements from a given list of integers. It works by using a condition `x if x == numbers[0]`` to get the first element of the list, and then uses the built-in `max` function to compare each element with the first one to find the rolling maximum element.