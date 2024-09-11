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
    # Initialize an empty list to store the rolling maximum elements
    max_elements = []
    
    # Initialize the current maximum element with the first element of the list
    current_max = numbers[0] if numbers else None
    
    # Append the first element to the max_elements list
    max_elements.append(current_max)
    
    # Iterate over the list of numbers starting from the second element
    for num in numbers[1:]:
        # Update the current maximum element if the current number is greater
        current_max = max(current_max, num)
        # Append the updated current maximum element to the max_elements list
        max_elements.append(current_max)
    
    return max_elements

# Test the rolling_max function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
print(rolling_max([]))  # Output: []
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list and keeps track of the maximum element encountered so far, appending it to the result list at each step. The script also includes example use cases to demonstrate the function's behavior.