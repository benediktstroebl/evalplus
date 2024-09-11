### Rolling Maximum Function
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

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    max_so_far = float('-inf')

    for num in numbers:
        if num >= max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list
```

### Example Usage
```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 1, 4, 3, 2]))  # Output: [5, 5, 4, 4, 4]
print(rolling_max([2, 1, 0, -1, -2]))  # Output: [2, 2, 2, 2, 2]
```