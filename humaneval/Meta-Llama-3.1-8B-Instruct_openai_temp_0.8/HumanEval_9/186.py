### Rolling Max Function
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

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
    
    # Initialize the rolling maximum list with the first element of the input list
    rolling_max_list = [numbers[0]]
    
    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # Update the rolling maximum list by appending the maximum of the current number and the last element in the list
        rolling_max_list.append(max(num, rolling_max_list[-1]))
    
    return rolling_max_list
```

### Example Usage
```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 4, 3, 2, 1]
print(rolling_max([]))  # Output: []
```