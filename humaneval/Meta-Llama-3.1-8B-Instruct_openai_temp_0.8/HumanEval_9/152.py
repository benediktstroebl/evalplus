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
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we define a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum number seen so far in the input list. The function starts by checking if the input list is empty, in which case it returns an empty list. If the list is not empty, it initializes `max_so_far` to the first element of the list and `result` with this maximum value. It then iterates through the rest of the list, updating `max_so_far` whenever a larger number is found and appending this maximum value to `result`. Finally, it returns `result`, which contains the rolling maximum elements.