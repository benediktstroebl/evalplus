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
    if not numbers:  # check if the input list is empty
        return []

    rolling_max_list = [numbers[0]]  # initialize the rolling max list with the first element
    current_max = numbers[0]

    for num in numbers[1:]:  # iterate over the rest of the list
        if num >= current_max:  # if the current number is greater than or equal to the current max
            current_max = num  # update the current max
        rolling_max_list.append(current_max)  # append the current max to the rolling max list

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```