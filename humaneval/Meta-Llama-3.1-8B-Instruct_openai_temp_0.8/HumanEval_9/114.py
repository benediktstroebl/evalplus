### Rolling Maximum Elements
#### Problem Description
Generate a list of rolling maximum elements found until each moment in a given sequence of integers.

#### Solution

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
    result = []  # Initialize an empty list to store the rolling max elements

    for num in numbers:
        if num >= max_so_far:  # If current number is greater than or equal to max_so_far
            max_so_far = num  # Update max_so_far
        result.append(max_so_far)  # Append max_so_far to the result list

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a variable `max_so_far` to keep track of the maximum element seen so far, and it appends `max_so_far` to the result list at each iteration of the loop. The example usage demonstrates how to call the `rolling_max` function with a sample input list and print the output.