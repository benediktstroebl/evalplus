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

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 3, 1, 2, 4]))  # Output: [5, 5, 5, 5, 5]
print(rolling_max([]))  # Output: []
```

In this code:

*   We start by checking if the input list `numbers` is empty. If it is, we return an empty list.
*   We initialize the `max_so_far` variable with the first element of the list and the `result` list with this maximum value.
*   We iterate over the list starting from the second element (at index 1). For each element, we update `max_so_far` if the current element is greater. We then append `max_so_far` to the `result` list.
*   Finally, we return the `result` list containing the rolling maximum values.