### Rolling Maximum Script
#### Problem Description
The script generates a list of rolling maximum elements found until a given moment in the sequence.

#### Code
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment in the sequence.

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
    result = [numbers[0]]

    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
            result.append(max_so_far)
        else:
            result.append(max_so_far)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```
#### Explanation
This script uses a simple iterative approach to solve the problem. It initializes the `max_so_far` variable with the first element of the list and the `result` list with the first element. Then, it iterates over the rest of the list. If it encounters a number greater than or equal to `max_so_far`, it updates `max_so_far` and appends it to the `result` list. Otherwise, it appends the current `max_so_far` to the `result` list.