Here's a self-contained Python function that provides the solution to the markdown code block problem:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x, _ in enumerate(sorted(numbers)) if numbers[x] > numbers[x+1]]
```
This function utilizes a generator expression to calculate the rolling maximum elements, it iterates through the sorted numbers and checks if each current element is greater than the next one, effectively finding the maximum element in each rolling window.