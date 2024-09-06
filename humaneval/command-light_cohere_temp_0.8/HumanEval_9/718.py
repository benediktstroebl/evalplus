Here's the self-contained Python function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in a given list of integers. """
    This time list comprehension is used to find the maximum element in each rolling window, 
    and the list is updated accordingly.
    >>> [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [x for x in numbers if type(x) == int]  # Convert list to list of integers
    rolling_maxes = [max(numbers[:i + 1]) for i in range(len(numbers))]
    return rolling_maxes
```
This function takes a list of integers as input and returns a list of rolling maximum elements found in the sequence. It does this by using list comprehension to find the maximum element in each rolling window of the list, where each window starts from index 0. The list comprehension creates a list of maximum elements in each rolling window and returns it as the output.