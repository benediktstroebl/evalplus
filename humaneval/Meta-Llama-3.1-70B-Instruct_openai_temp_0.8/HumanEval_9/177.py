```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum.
    """
    if not numbers:
        return []

    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Initialize the current maximum with the first element of the input list
    current_max = numbers[0]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # Update the current maximum if the current number is larger
        current_max = max(current_max, num)
        # Append the current maximum to the result list
        result.append(current_max)

    return result


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of integers representing the rolling maximum. It iterates over the input list, keeping track of the current maximum and appending it to the result list at each step. The function is documented with a docstring and includes an example usage.