```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum element found until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([]))  # []
print(rolling_max([5]))  # [5]
print(rolling_max([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(rolling_max([1, 1, 1, 1]))  # [1, 1, 1, 1]
print(rolling_max([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(rolling_max([5, 4, 3, 2, 1]))  # [5, 5, 5, 5, 5]
```