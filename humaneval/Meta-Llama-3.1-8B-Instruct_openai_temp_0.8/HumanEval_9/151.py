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
    if not numbers:  # Check if the input list is empty
        return []

    rolling_max_list = [numbers[0]]  # Initialize the rolling max list with the first element
    for num in numbers[1:]:  # Iterate over the list starting from the second element
        rolling_max_list.append(max(rolling_max_list[-1], num))  # Update the rolling max list

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iteration approach to build the rolling max list, starting from the first element of the input list and updating the list at each iteration with the maximum of the previous maximum and the current number. The function also includes a check for an empty input list and returns an empty list in this case.