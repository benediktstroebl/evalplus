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
    if not numbers:  # check if the list is empty
        return []

    max_so_far = numbers[0]  # initialize max_so_far with the first element
    rolling_max_list = [max_so_far]  # initialize the result list with the max_so_far

    for num in numbers[1:]:  # iterate over the list starting from the second element
        if num > max_so_far:  # if current number is greater than max_so_far
            max_so_far = num  # update max_so_far
        rolling_max_list.append(max_so_far)  # append max_so_far to the result list

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple iterative approach to keep track of the maximum number seen so far and appends it to the result list. It initializes `max_so_far` with the first element of the list and then iterates over the rest of the list, updating `max_so_far` whenever it encounters a larger number. The updated `max_so_far` is then appended to the result list.