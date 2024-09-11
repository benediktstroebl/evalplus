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

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = [numbers[0]]
    max_until_now = numbers[0]

    for num in numbers[1:]:
        if num > max_until_now:
            max_until_now = num
        rolling_max_list.append(max_until_now)

    return rolling_max_list


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
In this script, we first initialize a list `rolling_max_list` with the first element of `numbers`, and we also initialize `max_until_now` to the first element of `numbers`. Then we iterate over the rest of `numbers`. If the current number is greater than `max_until_now`, we update `max_until_now` to the current number. We append `max_until_now` to `rolling_max_list` at each iteration. Finally, we return `rolling_max_list`. This solution has a time complexity of O(n), where n is the number of elements in `numbers`.