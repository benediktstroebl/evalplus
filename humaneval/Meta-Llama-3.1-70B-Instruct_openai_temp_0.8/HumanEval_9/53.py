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
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_max_list = [max_so_far]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list


# Test cases
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Expected output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 4, 3, 2, 1]))  # Expected output: [5, 5, 5, 5, 5]
print(rolling_max([1, 1, 1, 1, 1]))  # Expected output: [1, 1, 1, 1, 1]
print(rolling_max([]))  # Expected output: []
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the maximum so far with the first element of the list and then iterates over the rest of the list, updating the maximum so far whenever it encounters a larger number. The rolling maximum list is updated at each step with the current maximum so far. The function returns the rolling maximum list. The script also includes test cases to verify the correctness of the function.