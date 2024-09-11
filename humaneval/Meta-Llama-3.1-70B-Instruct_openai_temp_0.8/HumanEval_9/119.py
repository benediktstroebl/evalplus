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


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script works by maintaining a `max_num` variable to keep track of the maximum number encountered so far, and appending this maximum number to the `rolling_max_list` at each step. When a new number is encountered that is larger than the current `max_num`, `max_num` is updated to this new number. The `rolling_max_list` is then returned at the end of the function.

Alternatively, you could use the `itertools.accumulate` function with the `max` function to achieve the same result in a more concise way:

```python
import itertools
import operator

def rolling_max(numbers: List[int]) -> List[int]:
    return list(itertools.accumulate(numbers, max))
```

This version works by using `itertools.accumulate` to calculate the cumulative maximum of the input list, which is equivalent to the rolling maximum. The `operator.max` function is used to specify the operation to be applied at each step. The result is converted back to a list before being returned.