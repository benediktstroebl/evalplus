```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers

    Returns:
        A list of rolling maximum elements

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:  # Check if the list is empty
        return []
    
    result = [numbers[0]]  # Initialize the result list with the first element
    max_so_far = numbers[0]  # Initialize the maximum element found so far
    
    for num in numbers[1:]:  # Iterate over the list starting from the second element
        if num >= max_so_far:  # If the current element is greater than or equal to the max_so_far
            max_so_far = num  # Update max_so_far
        result.append(max_so_far)  # Append max_so_far to the result list
    
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([]))  # Output: []
print(rolling_max([5]))  # Output: [5]
```

This Python function `rolling_max` takes a list of integers as input and returns a new list where each element is the maximum element seen so far in the original list. The function uses a single pass through the input list, maintaining a running maximum as it goes, to build the output list. The function also checks for the edge case where the input list is empty, in which case it returns an empty list.