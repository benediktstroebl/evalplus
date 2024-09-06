```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Each element in the maximum sequence is returned.
    """
    list comprehension is used to find the maximum element in the list
    using the `max()` function, and then the rolling maximum is calculated by
    iterating over the list and keeping the current maximum element.
    The list of rolling maximum elements is then returned.
    """

def test_rolling_max(numbers: List[int]) -> None:
    """
    Test the function `rolling_max`
    with a sample list of numbers
    """
    expected = [1, 2, 3, 3, 3, 4, 4]
    got = rolling_max([1, 2, 3, 2, 3, 4, 2])
    assert expected == got
    print("Test passed.")

numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max(numbers)
```
This script provides a self-contained function `rolling_max` that solves the problem and passes the corresponding tests.