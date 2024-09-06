```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function generates a list of rolling maximum elements from a given list of integers.
    Return a list of rolling maximum elements found until the given moment in the sequence.
    Input: numbers : list of integers
    Output: list of integers
    """
    return [x for x, i in zip(numbers, numbers[1:]) if i < len(numbers) and numbers[i] > numbers[i-1]]

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```