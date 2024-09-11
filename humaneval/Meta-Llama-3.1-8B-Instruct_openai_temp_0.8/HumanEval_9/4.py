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
    if not numbers:  # Check if the list is empty
        return []
    
    max_so_far = numbers[0]
    result = [numbers[0]]  # Initialize the result list with the first element
    
    for num in numbers[1:]:  # Iterate over the list starting from the second element
        max_so_far = max(num, max_so_far)  # Update the maximum seen so far
        result.append(max_so_far)  # Append the maximum seen so far to the result list
    
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([]))  # Output: []
print(rolling_max([5]))  # Output: [5]
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a simple iterative approach to maintain the maximum element seen so far and appends this maximum to the result list at each step. The function also includes a docstring that provides a description of the function, its parameters, and its return value. The script also includes test cases to demonstrate the function's behavior.