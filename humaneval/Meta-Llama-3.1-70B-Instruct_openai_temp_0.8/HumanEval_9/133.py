```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers, where each element is the maximum of the elements in the input list up to that point.
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_maxes = [max_so_far]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_maxes.append(max_so_far)

    return rolling_maxes


# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test cases
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
print(rolling_max([1, 1, 1, 1, 1]))  # Output: [1, 1, 1, 1, 1]
print(rolling_max([]))  # Output: []
```