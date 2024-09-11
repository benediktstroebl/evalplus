### Rolling Maximum Function in Python
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
    max_so_far = float('-inf')  # Initialize max_so_far as negative infinity
    result = []  # Initialize an empty list to store results

    for num in numbers:
        if num >= max_so_far:  # If current number is greater than max_so_far
            max_so_far = num  # Update max_so_far
        result.append(max_so_far)  # Append max_so_far to the result list

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function called `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates through the input list, keeping track of the maximum element seen so far and updating the result list with the maximum element at each position. The example usage demonstrates how to call the function with a sample list and print the result.