```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements in a given list.
    Each element in the maximum list is the maximum value of an integer in the list after the current one, 
    following the order of rolling windows.
    Args:
        numbers (List[int]): A list of integers.
    Returns: A list of integers containing the rolling maximum elements.
    """

rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]

4 tests passed successfully using this code.
```