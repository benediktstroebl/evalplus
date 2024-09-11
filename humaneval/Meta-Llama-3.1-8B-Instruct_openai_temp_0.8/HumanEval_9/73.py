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
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    max_found = numbers[0]

    for num in numbers[1:]:
        if num >= max_found:
            rolling_max_list.append(num)
            max_found = num
        else:
            rolling_max_list.append(max_found)

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([]))  # Output: []
print(rolling_max([1]))  # Output: [1]
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
```