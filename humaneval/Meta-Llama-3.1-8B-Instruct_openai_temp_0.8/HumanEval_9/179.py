### Rolling Maximum Script
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers

    Returns:
    List[int]: A list of rolling maximum elements

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum elements
    rolling_max_list = []
    
    # Initialize the maximum element to the first element of the list
    max_element = numbers[0]
    
    # Iterate over the list of numbers
    for num in numbers:
        # If the current number is greater than the maximum element, update the maximum element
        if num > max_element:
            max_element = num
        # Append the maximum element to the list
        rolling_max_list.append(max_element)
    
    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list, updating the maximum element whenever it finds a larger number, and appending the maximum element to the list at each step. The function returns the list of rolling maximum elements. The script includes a test case to demonstrate the function's behavior.