```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers: A list of integers.

    Returns:
    A list of rolling maximum elements.
    """
    
    # Initialize an empty list to store the rolling max values
    rolling_max_values = []
    
    # Initialize the current max value to negative infinity
    current_max = float('-inf')
    
    # Iterate over each number in the input list
    for num in numbers:
        # Update the current max value if the current number is greater
        current_max = max(current_max, num)
        
        # Append the current max value to the result list
        rolling_max_values.append(current_max)
    
    # Return the list of rolling max values
    return rolling_max_values

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```