```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return a list of rolling max elements from the given list.
    """
    max_so_far = numbers[0]
    rolling_maxes = [max_so_far]

    for num in numbers[1:]:
        current = max(num, max_so_far)
        max_so_far = current
        rolling_maxes.append(current)

    return rolling_maxes
    """

def test_rolling_max():
    numbers = [1, 2, 3, 2, 3]
    assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4], "Wrong rolling_max output"

# Test the function
test_rolling_max()
```

This script defines a `rolling_max` function that calculates and returns a list of rolling maximum elements from a given list of integers. It also includes a test function to verify the correctness of the `rolling_max` function.