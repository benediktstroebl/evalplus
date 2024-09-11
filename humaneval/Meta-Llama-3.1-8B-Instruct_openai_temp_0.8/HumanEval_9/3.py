```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of rolling maximum elements

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num >= max_so_far:
            result.append(num)
            max_so_far = num
        else:
            result.append(max_so_far)

    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([]))  # Output: []
print(rolling_max([5]))  # Output: [5]
print(rolling_max([1, 1, 1, 1, 1]))  # Output: [1, 1, 1, 1, 1]
```

In this code:

*   We initialize the `result` list with the first element of the input list `numbers`.
*   We maintain the maximum element seen so far in `max_so_far`.
*   We iterate through the list `numbers` starting from the second element (index 1).
*   For each element, we check if it's greater than or equal to the current `max_so_far`.
    *   If it is, we append it to the result list and update `max_so_far`.
    *   If it's not, we append the current `max_so_far` to the result list.
*   Finally, we return the result list, which contains the rolling maximum elements for each position in the input list.