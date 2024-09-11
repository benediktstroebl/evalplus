```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum element found until given moment in the sequence.
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    max_num = numbers[0]

    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        rolling_max_list.append(max_num)

    return rolling_max_list


# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```