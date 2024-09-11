```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:  # Check if the list is empty
        return []

    max_so_far = numbers[0]  # Initialize the maximum element so far
    rolling_max_list = [max_so_far]  # Initialize the result list

    for num in numbers[1:]:  # Iterate over the rest of the list
        if num > max_so_far:  # If the current number is greater than the maximum so far
            max_so_far = num  # Update the maximum so far
        rolling_max_list.append(max_so_far)  # Append the maximum so far to the result list

    return rolling_max_list


# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that calculates the rolling maximum element in a given list of integers. It uses a simple iterative approach, keeping track of the maximum element so far and updating it whenever a larger element is encountered. The function returns a list of rolling maximum elements.

The script also includes an example usage of the function, demonstrating its behavior on the provided example input.