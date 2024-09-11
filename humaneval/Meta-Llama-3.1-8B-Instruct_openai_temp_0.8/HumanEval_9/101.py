### Rolling Maximum Elements
#### Problem Statement
From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')  # Initialize max_so_far as negative infinity
    result = []  # Initialize an empty list to store the rolling maximum elements

    for num in numbers:
        if num >= max_so_far:  # If current number is greater than or equal to max_so_far
            max_so_far = num  # Update max_so_far
        result.append(max_so_far)  # Append max_so_far to the result list

    return result  # Return the result list


# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This solution iterates over the input list of numbers, keeping track of the maximum number encountered so far (`max_so_far`). For each number, it checks if it's greater than or equal to `max_so_far`. If it is, it updates `max_so_far` to the current number. Finally, it appends `max_so_far` to the result list. The result list contains the rolling maximum elements found until the end of the sequence.