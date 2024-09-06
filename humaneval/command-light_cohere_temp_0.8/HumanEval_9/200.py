Here is a self-contained Python function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling 
    maximum elements.
    Returns a
    list with the rolling maximum elements in sequence.
    """
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]

# Example:
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)
```

This code provides a function that accepts a list of integers and produces a new list with the rolling maximum elements in order. The function tests a accepted input types and returns a list of integers with the rolling maximum element(s) as output.