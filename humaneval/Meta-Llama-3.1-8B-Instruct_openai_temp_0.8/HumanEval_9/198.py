### Rolling Maximum Element

Here's a Python solution to the problem using a list comprehension with a simple and efficient algorithm.

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
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]
    
    # Iterate over the rest of the list and update the result list with the maximum of the current element
    # and the last element in the result list
    for num in numbers[1:]:
        result.append(max(num, result[-1]))
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input, and returns a new list where each element is the rolling maximum element found until that moment in the sequence. The function uses a simple and efficient algorithm to calculate the rolling maximum elements in linear time. The example usage demonstrates how to use the function with the given example list.