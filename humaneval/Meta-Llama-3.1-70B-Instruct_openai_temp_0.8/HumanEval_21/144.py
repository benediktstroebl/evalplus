```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the given list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A list of float numbers where the smallest number is 0 and the largest is 1.
    """
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the range of values
    range_value = max_value - min_value
    
    # If the range is zero, return a list of zeros
    if range_value == 0:
        return [0.0] * len(numbers)
    
    # Apply the linear transformation
    rescaled_numbers = [(num - min_value) / range_value for num in numbers]
    
    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers as input, calculates the minimum and maximum values, and applies a linear transformation to rescale the numbers such that the smallest number becomes 0 and the largest becomes 1. It includes example usage and handles edge cases where the range of values is zero.