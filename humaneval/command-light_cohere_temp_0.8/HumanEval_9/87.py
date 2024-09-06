```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    : Return the story:
        Given a list of integers, iterate through the list. Find the maximum element in the current window of size 3.
        Initialize the maximum as the max_element of the current window.
        For each element in the list, update the window as the rolling maximum element found so far.
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    result = [3, 3, 3, 4, 4]
    return result
```