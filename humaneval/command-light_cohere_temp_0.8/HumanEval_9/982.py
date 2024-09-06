```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling 
    maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x in numbers if x > max_element(numbers, i) for i in range(len(numbers))]

def max_element(numbers: List[int], i: int) -> int:
    """
    Calculates the maximum element in the list at the current 
    position.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> max_element(numbers, 0) = 3
    """
    return max(numbers[i], numbers[i+1])
```