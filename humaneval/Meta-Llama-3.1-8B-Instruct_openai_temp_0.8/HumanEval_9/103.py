### Rolling Maximum Elements

The following Python script calculates the rolling maximum elements in a given list of integers.

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
    rolling_max_list = [max_so_far]
    
    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)
    
    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script initializes `max_so_far` with the first element of the list and appends it to the `rolling_max_list`. Then it iterates over the rest of the list. If it encounters a number greater than `max_so_far`, it updates `max_so_far` to that number. The updated `max_so_far` is then appended to the `rolling_max_list`. This way, the script generates the list of rolling maximum elements in the given list.