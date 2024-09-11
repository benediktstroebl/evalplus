### Rolling Maximum Sequence
#### A Python function to generate a list of rolling maximum elements from a given sequence.

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
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than or equal to the last number in the result list,
        # update the result list
        if num >= result[-1]:
            result.append(num)
        # Otherwise, keep the last number in the result list
        else:
            result.append(result[-1])

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a simple iterative approach to maintain the rolling maximum at each position in the sequence. The test case at the end demonstrates the function's behavior on a sample input.