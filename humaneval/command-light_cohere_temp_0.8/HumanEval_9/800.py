```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function generates a list of rolling maximum elements from a given list of integers.
    The rolling maximum is the sequence of elements as the maximum element from the sequence when we
    move one step ahead.
    Returns a max sequence of numbers in a list.
    """ numbers: List[int for i in range(len(numbers))]) -> List[int]
    numbers = [3, 2, 4, 1, 3, 2]
    return [max(numbers[i:]) for i in range(len(numbers)))]
```