Here's a Python script that solves the problem:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    Args:
    numbers: A list of integers
    
    Returns:
    A list of rolling maximum elements
    
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    
    # Initialize a list to store the rolling maximum elements
    rolling_max_list = []
    
    # Initialize the maximum element to negative infinity
    max_element = float('-inf')
    
    # Iterate through each number in the input list
    for num in numbers:
        # If the current number is greater than the max element, update the max element
        if num > max_element:
            max_element = num
        
        # Append the max element to the result list
        rolling_max_list.append(max_element)
    
    # Return the list of rolling maximum elements
    return rolling_max_list

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the rolling maximum element found so far in the sequence. The function uses a simple iterative approach to keep track of the maximum element as it iterates through the input list.