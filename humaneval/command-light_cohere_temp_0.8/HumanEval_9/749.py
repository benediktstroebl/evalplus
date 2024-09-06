```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found in the given list.
    """
    list of integers is passed to the function. Each number is the rolling max from the numbers list,
    and the index of the list is incremented by 1. The rolling max of the elements is stored in a list and returned.
    """
Test case:
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    rolling_max(test_numbers)
    assert rolling_max(test_numbers) == [1, 2, 3, 4, 5, 6, 7, 8]
```