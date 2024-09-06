```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling max elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x, _ in zip(numbers, numbers[1:]) if x > numbers[_]]
``` 
This function is a self-contained Python solution that utilizes the `zip` function to find the rolling maximum elements in a list of integers.