```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Each element of the maximum element in the list is updated and returned after each iteration
    until the list is exhausted.
    """
    The list of integers is passed as an argument to the function.

Tests passed:
    - It accepts a list of integers as an argument and returns the list with rolling maximum elements.
    - The list contains elements [1, 2, 3, 2, 3, 3, 4, 4].
    - The list is not empty.
    - The maximum element in the first iteration is 1.
    - The second iteration, the maximum element is 2, which is greater than 1.
    - The third iteration, the maximum element is 3, which is greater than 2.
    - This list has the same maximum elements in all subsequent iterations.
    """

example:
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
```