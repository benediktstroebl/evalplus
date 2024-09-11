### Rolling Maximum Elements
#### Problem Description
Given a list of integers, generate a list of rolling maximum elements found until each moment in the sequence.

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
    max_elements = []
    current_max = float('-inf')  # Initialize current max as negative infinity

    for num in numbers:
        if num > current_max:
            current_max = num
        max_elements.append(current_max)

    return max_elements

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a simple iterative approach:

1. Initialize an empty list `max_elements` to store the rolling maximum elements and a variable `current_max` to keep track of the current maximum element.
2. Iterate through the input list `numbers`.
3. For each number, check if it is greater than the current maximum. If it is, update the current maximum.
4. Append the current maximum to the `max_elements` list.
5. Return the `max_elements` list.

The example usage demonstrates how to call the `rolling_max` function with a sample input list and print the output.