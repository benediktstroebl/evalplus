```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_maxes = [max_so_far]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_maxes.append(max_so_far)

    return rolling_maxes

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of the rolling maximum elements found until each moment in the sequence. The function iterates over the input list, keeping track of the maximum element seen so far and appending it to the output list at each step. If a new maximum element is found, it updates the `max_so_far` variable. The script includes an example usage of the function with a list of numbers.