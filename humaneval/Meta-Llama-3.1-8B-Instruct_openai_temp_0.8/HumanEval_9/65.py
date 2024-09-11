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
    # Initialize an empty list to store the rolling maximums
    rolling_maxes = []
    
    # Initialize the maximum found so far as the first element in the list
    max_found = numbers[0]
    
    # Iterate over each number in the list
    for num in numbers:
        # If the current number is greater than the max found so far, update max_found
        if num > max_found:
            max_found = num
        # Append the max_found to the rolling_maxes list
        rolling_maxes.append(max_found)
    
    # Return the list of rolling maximums
    return rolling_maxes

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over each number in the input list, keeping track of the maximum value seen so far. It appends this maximum value to the output list after processing each number. Finally, it returns the list of rolling maximums.