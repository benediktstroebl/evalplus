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
    rolling_max_list = []
    
    # Initialize the maximum with the first number in the list
    max_so_far = numbers[0]
    
    # Iterate over the list of numbers
    for num in numbers:
        # If the current number is greater than the max_so_far, update max_so_far
        if num > max_so_far:
            max_so_far = num
        
        # Append the max_so_far to the rolling_max_list
        rolling_max_list.append(max_so_far)
    
    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```