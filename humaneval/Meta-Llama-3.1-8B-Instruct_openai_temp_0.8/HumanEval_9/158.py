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

    result = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num >= max_so_far:
            result.append(num)
            max_so_far = num
        else:
            result.append(max_so_far)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Expected output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([4, 2, 5, 1, 3]))  # Expected output: [4, 4, 5, 5, 5]
print(rolling_max([]))  # Expected output: []
```

In this script, the `rolling_max` function takes a list of integers as input and returns a new list where each element is the maximum of the current and all previous elements in the original list. The function iterates over the input list, keeps track of the maximum element seen so far, and appends the maximum of the current element and the maximum seen so far to the result list. If the current element is greater than or equal to the maximum seen so far, it updates the maximum seen so far and appends the current element to the result list. Otherwise, it appends the maximum seen so far to the result list. The function returns the result list at the end.