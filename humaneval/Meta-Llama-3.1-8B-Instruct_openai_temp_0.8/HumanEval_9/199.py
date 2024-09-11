### Rolling Maximum Elements in a Sequence

Here is a Python script that implements the `rolling_max` function, which generates a list of rolling maximum elements found until a given moment in the sequence.

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
    rolling_max_list = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_list.append(max_so_far)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which takes a list of integers as input and returns a list of rolling maximum elements found until a given moment in the sequence. The function initializes the `max_so_far` variable with the first element of the input list and the `rolling_max_list` with the first element of the input list. It then iterates through the input list starting from the second element, updating the `max_so_far` variable to be the maximum of the current `max_so_far` and the current number, and appending the updated `max_so_far` to the `rolling_max_list`. Finally, the function returns the `rolling_max_list`.

The script includes an example usage of the `rolling_max` function, where it prints the rolling maximum elements for the input list `[1, 2, 3, 2, 3, 4, 2]`, resulting in `[1, 2, 3, 3, 3, 4, 4]`.