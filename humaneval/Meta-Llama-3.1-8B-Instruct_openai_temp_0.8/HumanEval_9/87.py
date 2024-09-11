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
    rolling_max_list = []
    
    # Initialize the maximum element with the first element in the list
    max_element = numbers[0]
    
    # Iterate over each element in the list
    for num in numbers:
        # Update the maximum element if the current element is greater
        if num > max_element:
            max_element = num
        # Append the maximum element to the list
        rolling_max_list.append(max_element)
    
    # Return the list of rolling maximum elements
    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a single loop to iterate over the input list and keeps track of the maximum element seen so far, appending it to the result list at each step. The function is then tested with a sample input to demonstrate its correctness.