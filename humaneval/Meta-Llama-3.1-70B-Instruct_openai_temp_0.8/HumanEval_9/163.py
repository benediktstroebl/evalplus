```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum element found until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_max_values = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_values.append(max_so_far)

    return rolling_max_values


# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function called `rolling_max` which takes a list of integers and returns a new list where each element is the maximum of all elements in the input list up to that point. The function uses a for loop to iterate over the input list, keeping track of the maximum value seen so far and appending it to the result list at each step. The script also includes a docstring that provides documentation for the function, including an example usage.