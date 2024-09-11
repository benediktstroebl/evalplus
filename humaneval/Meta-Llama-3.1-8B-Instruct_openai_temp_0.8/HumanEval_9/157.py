### Rolling Maximum
#### Python Script

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
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple algorithm to calculate the rolling maximum of a given list of numbers. It starts by checking if the input list is empty, in which case it returns an empty list. Then, it initializes `max_so_far` to the first element of the list and `result` to a list containing `max_so_far`.

The script then iterates over the rest of the list, updating `max_so_far` to be the maximum of its current value and the current number. It also appends `max_so_far` to the `result` list at each iteration. Finally, it returns the `result` list.