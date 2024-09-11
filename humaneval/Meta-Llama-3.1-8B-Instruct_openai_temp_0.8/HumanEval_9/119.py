### Rolling Maximum Function

The following Python script defines a function `rolling_max` that generates a list of rolling maximum elements found until a given moment in the sequence.

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

    rolling_max_list = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num >= current_max:
            rolling_max_list.append(num)
            current_max = num
        else:
            rolling_max_list.append(current_max)

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

This script uses a simple iterative approach to maintain a list of rolling maximum elements. It starts with the first element as the current maximum and then iterates through the rest of the list. If it encounters a number greater than or equal to the current maximum, it updates the current maximum and adds it to the list. If it encounters a number less than the current maximum, it simply adds the current maximum to the list. The function returns the list of rolling maximum elements.