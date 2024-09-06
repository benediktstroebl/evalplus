```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of the rolling maximum elements in a given list of integers.
    Parameters: List[int].
    Returns: List[int].
    """
    # Initialize a list of the maximum rolling elements found so far, and reset the index
    # where the next element will be found.
    memo = [[] for _ in range(len(numbers)):
        numbers.append(max(numbers[index:], numbers[index]))
        index = index + 1
    # Return a list of the maximum rolling elements
    return [max(n) for n in numbers]
```