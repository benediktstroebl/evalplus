```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence (default is 0).
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]"""
    numbers.sort()
    a max_num = max(numbers)
    rolling_max_elements = [max(numbers[i]) for i in range(len(numbers)) if numbers[i] > max_num]
    return rolling_max_elements

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
The code defines a function `rolling_max` that takes a list of integers as an argument and returns a new list containing the rolling maximum elements found in the input sequence up to the given moment.