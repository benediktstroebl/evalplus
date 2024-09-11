### Rolling Maximum Elements

This Python script generates a list of rolling maximum elements from a given list of integers.

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
    # Use a list comprehension with a conditional statement to compare each number with the rolling max
    return [max(numbers[:i+1]) for i in range(len(numbers))]

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

This script defines the `rolling_max` function, which takes a list of integers as input and returns a list of rolling maximum elements. The function uses a list comprehension with `max(numbers[:i+1])` to get the rolling maximum at each position. Finally, it tests the function with an example list and prints the result.