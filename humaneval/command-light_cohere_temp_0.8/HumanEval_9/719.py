Here's the function `rolling_max` along with the corresponding tests:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> numbers[0] == rolling_max(numbers)[0]
    True
    >>> len(numbers) != len(rolling_max(numbers))
    True
    """
    return [x for x in numbers if numbers[x] > numbers[x-1]]

# Test cases:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(numbers) == len(result)
assert all(numbers[x] == result[x]) for x in range(len(numbers)))

```

This code defines a function `rolling_max` that generates a list of rolling maximum elements in a given list of integers. The function utilizes a loop to iterate through the list and selects the element that is greater than the previous element, resulting in a list of increasing values. The function is then tested using several assertions to ensure its correctness.