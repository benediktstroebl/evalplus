```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function generates a list of rolling max elements from a given list of integers.
    Each element in the max rolling sequence will be the maximum value seen so far in the sequence.
    The function uses the max object to efficiently find the maximum value in each iteration of the rolling sequence.
    Return a list of integers in ascending order.
    """
    
    Args:
        numbers (List[int]): List of integers
    Returns:
        List[int]: List of rolling max elements
    """
    # Initialize result list with first element in the list
    rolling_max_sequence = [numbers[0]]
    
    # Iterate over the list, adding each number to the rolling sequence
    for num in numbers[1:]:
        rolling_max_sequence.append(max(rolling_max_sequence[-1], num))
    
    # Return the list of rolling max elements in ascending order
    return [num for num in rolling_max_sequence]
```