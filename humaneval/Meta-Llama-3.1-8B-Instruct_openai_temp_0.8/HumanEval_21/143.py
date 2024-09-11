```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
    numbers (List[float]): A list of floating point numbers
    
    Returns:
    List[float]: The input list with all numbers rescaled to the unit interval [0, 1]
    
    Raises:
    ValueError: If the input list contains less than two elements
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check if all numbers are equal to avoid division by zero
    if min_value == max_value:
        return [0.0] * len(numbers)
    
    # Apply linear transformation
    return [(n - min_value) / (max_value - min_value) for n in numbers]

# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script takes a list of floating point numbers, calculates the minimum and maximum values, and applies a linear transformation to the list such that the smallest number becomes 0 and the largest becomes 1. It includes a check to ensure the input list contains at least two elements and raises a ValueError if not. If all numbers in the list are equal, it returns a list of zeros.