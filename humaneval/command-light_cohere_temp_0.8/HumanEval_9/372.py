```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in a given list of integers.
    The rolling maximum element is the maximum value among all elements
    in the list, but only when that element is also present in the
    list for the current time step.
    Returns a maximum list where all the maximum values, one per step, and then the first one.
    the list is the list of all rolling maximum elements, regardless of their order.
    # type: List[int]
    """
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max = [max(numbers[i:]) for i in range(len(numbers)-1)]
print(rolling_max)  # Output: [3, 3, 3, 4, 4]
```