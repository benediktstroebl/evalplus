### Rolling Maximum Function in Python
#### Problem Description
Given a list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution
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
    result = []
    max_so_far = float('-inf')
    
    for number in numbers:
        if number > max_so_far:
            max_so_far = number
        result.append(max_so_far)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a new list with the rolling maximum elements. It initializes a variable `max_so_far` to negative infinity and iterates over the input list. For each number, it checks if the number is greater than the current `max_so_far`. If it is, it updates `max_so_far` to the current number. Then, it appends the current `max_so_far` to the result list. Finally, it returns the result list.