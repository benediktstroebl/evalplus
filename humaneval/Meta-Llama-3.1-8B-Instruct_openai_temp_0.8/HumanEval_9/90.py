### Rolling Maximum Calculation
#### Python Script

A Python function `rolling_max` is implemented to calculate the rolling maximum from a given list of integers.

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

    max_so_far = numbers[0]
    result = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)

    return result


# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    print(rolling_max(numbers))  # Expected output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input. It initializes the maximum so far with the first element of the list and the result list with this maximum. Then, it iterates over the rest of the list, updating the maximum so far and appending it to the result list at each step. The function returns the result list, which contains the rolling maximum elements.

The script includes an example usage in the `if __name__ == "__main__":` block to demonstrate how to use the `rolling_max` function.