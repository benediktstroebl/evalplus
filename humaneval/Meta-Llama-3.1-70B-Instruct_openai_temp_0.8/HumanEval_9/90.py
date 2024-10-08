```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers representing the rolling maximum at each position.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_max_values = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_values.append(max_so_far)

    return rolling_max_values


if __name__ == "__main__":
    print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
    print(rolling_max([]))  # Output: []
    print(rolling_max([5]))  # Output: [5]
    print(rolling_max([1, 1, 1, 1]))  # Output: [1, 1, 1, 1]
    print(rolling_max([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
    print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
```