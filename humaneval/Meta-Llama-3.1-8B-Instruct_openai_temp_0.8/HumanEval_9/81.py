```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum element found until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum elements
    max_elements = []
    
    # Initialize the maximum element as negative infinity
    max_element = float('-inf')
    
    # Iterate over each number in the input list
    for num in numbers:
        # Update the maximum element if the current number is greater
        max_element = max(max_element, num)
        
        # Append the maximum element to the list
        max_elements.append(max_element)
    
    # Return the list of rolling maximum elements
    return max_elements

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```