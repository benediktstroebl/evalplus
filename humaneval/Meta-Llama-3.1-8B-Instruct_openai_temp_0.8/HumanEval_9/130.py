**Rolling Maximum Problem Solution**
=====================================

Here is a Python script that solves the problem:

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = [max(numbers[:i+1]) for i in range(len(numbers))]
    return result
```

This script defines a function `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements. It uses a list comprehension to generate the result by finding the maximum element in the list up to each position.

**Example Usage**
---------------

```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This will output the expected result: `[1, 2, 3, 3, 3, 4, 4]`.