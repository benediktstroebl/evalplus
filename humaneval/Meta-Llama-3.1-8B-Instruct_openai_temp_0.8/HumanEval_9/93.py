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

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_elements = [max(numbers[:i+1]) for i in range(len(numbers))]
    return rolling_max_elements


# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that uses list comprehension to generate a list of rolling maximum elements from the input list `numbers`. It then tests the function with the provided example. The function has a time complexity of O(n^2) due to the use of the `max` function within the list comprehension, which can be optimized to O(n) using a different approach. However, the given implementation is straightforward and easy to understand. 

Here is a version of the function optimized to O(n) by keeping track of the maximum element seen so far:
```python
def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')
    result = []
    
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    
    return result


# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This optimized version maintains a list `result` to store the rolling maximum elements, and a variable `max_so_far` to track the maximum element seen so far. It iterates over the input list once, updating `max_so_far` and appending it to `result` at each step, resulting in a time complexity of O(n).