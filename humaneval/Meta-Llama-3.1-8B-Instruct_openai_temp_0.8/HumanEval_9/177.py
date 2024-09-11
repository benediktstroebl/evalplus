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
    """
    # Initialize an empty list to store the rolling maximum values
    rolling_max_values = []
    
    # Initialize the maximum value with the first element in the list
    max_value = numbers[0]
    
    # Add the first maximum value to the list
    rolling_max_values.append(max_value)
    
    # Iterate over the list starting from the second element
    for num in numbers[1:]:
        # Update the maximum value if the current number is greater
        if num > max_value:
            max_value = num
        
        # Add the maximum value to the list
        rolling_max_values.append(max_value)
    
    return rolling_max_values

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found until the given moment in the sequence. The function uses a simple iterative approach to keep track of the maximum value seen so far and updates it whenever a larger number is encountered. The final list of rolling maximum values is returned by the function.